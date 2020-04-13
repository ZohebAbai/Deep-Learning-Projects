from flask import Flask, render_template, request
from PIL import Image
import imageio
import numpy as np
from tensorflow.keras.models import load_model
import re, sys, os, base64

class_idx = ['0','1','2','3','4','5','6','7','8','9',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

app = Flask(__name__)

@app.route('/')
def index_view():
    return render_template('index.html')

def convertImage(imgData1):
    imgstr = re.search(b'base64,(.*)',imgData1).group(1)
    with open('output.png','wb') as output:
        output.write(base64.b64decode(imgstr))

@app.route('/predict/',methods=['GET','POST'])
def predict():
    imgData = request.get_data()
    convertImage(imgData)
    x = imageio.imread('output.png',pilmode='L')
    x = np.invert(x)
    x = np.array(Image.fromarray(x).resize((28,28), Image.ANTIALIAS))
    x = x.reshape(1,28,28,1)
    x = np.true_divide(x, 255)
    model = load_model("./model/model.h5")
    scores = model.predict(x)
    index = np.argmax(scores)
    response = str(class_idx[index])
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
