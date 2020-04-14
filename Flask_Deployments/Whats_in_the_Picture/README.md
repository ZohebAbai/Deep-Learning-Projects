# Whats_in_the_Picture

AI describing an Image.

This app cannot be deployed on Heroku due to two reasons:
    1. **Slug Size:** Heroku provides a max slug size of 500 MB, the total data an app can hold after compression. This app requires around 250 MB while deployment and extra 528 MB (VGG pre-trained weights) while running.
    2. **Request TimeOut:** Due to large sized pre-trained model the PUT request shows time out and app does not lands to result page.

You can try deploying it in AWS, Paperspace or GCloud but they all charge you per hour for the machine and for the storage, Heroku is better option comparatively.

It runs fine on local machine. Try running it.
