import os
from werkzeug.utils import secure_filename
from pickle import load
from tensorflow.keras.models import load_model
from flask import Flask, request, render_template
from predict import *

# pre-define the max sequence length (from training)
max_length = 34

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
	if request.method == 'GET':
		return render_template('index.html', value='Home')
	if request.method == 'POST':
		print(request.files)
		if 'file' not in request.files:
			print('Image not uploaded')
			return
		image = request.files['file']
		image.save(os.path.join('images', secure_filename(image.filename)))
		feature = extract_features(str('./images/'+image.filename))
		# load model and tokenizer
		tokenizer = load(open('./model/tokenizer.pkl', 'rb'))
		model = load_model('./model/model_4.h5')
		description = generate_desc(model, tokenizer, feature, max_length)
		return render_template('result.html', description=description[8:-6])

if __name__ == '__main__':
	app.run(debug=True, port=8000, host='0.0.0.0')
