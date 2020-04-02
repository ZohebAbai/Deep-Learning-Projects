# Aerial Images Segmentation

Automatic Pixelwise Labelling of Aerial Imagery based on [Inria Aerial Image Labeling Contest.](https://project.inria.fr/aerialimagelabeling/contest/)

It was a part of our [Fellowship.ai](https://fellowship.ai/) demo project, consisting of three 3 members Me, Jhansi and Pallavi. Submitted on June 1, 2019 [we achieved one of the top results on the leaderboard back then.](https://project.inria.fr/aerialimagelabeling/leaderboard/)

This notebooks is private in [Fellowship.ai repository](https://github.com/fellowship) but as its almost an year now, I am making it publicly available at my repository.

## Dataset
The dataset includes urban settlements over the United States and Austria, and is labeled into building and not building classes. Contrary to all previous datasets, the training and test sets are split by city instead of excluding random pixels or tiles.

![Images with their reference](https://github.com/ZohebAbai/Deep-Learning-Projects/blob/master/Pytorch_Fastai/Aerial-Images-Segmentation/Dataset%20images%20with%20reference.png)

|Train| Tiles | Test | Tiles|
|:------|:----|-----:|-----:|
|Austin, TX | 36 |Bellingham, WA |36|
|Chicago, IL | 36 | San Francisco, CA| 36 |
|Kitsap County, WA | 36 | Bloomington, IN |36|
|Vienna, Austria | 36 |Innsbruck, Austria |36|
|West Tyrol, Austria | 36 | East Tyrol, Austria| 36|
|Total | 180 | Total | 180|

Validation set is created from Training dataset by separating the first five tiles of each area from the training set (e.g. Austin{1-5}).

## Problem Statement
In a given aerial image, identify and mark the presence of buildings i.e. classify at a pixel level of the aerial images if it belongs to the building class or not. The challenge is to design methods that generalize to different areas of the earth, considering the important intra-class variability encountered over large geographic extents.

## Steps

### 1. Preprocessing the data:
Two approaches are implemented to preprocess the image files due to large size of images (5k X 5k).
1. Resize the images offline to a lower dimension (512x512) using bilinear interpolation technique and save the resulting images to drive, inorder to avoid repeated conversions.
2. Generate patches of lower dimension (250x250) with no overlapping pixels with a sliding window logic both for .jpg and .tif formats, and save the generated patches to drive, to avoid repeated operations.
3. Generate patches of lower dimension (256x256) with overlapping of 6 pixels and padding of 3 pixels with a sliding window logic for .tif formats, and save the generated patches to drive, to avoid repeated operations.

### 2. Model building
Once we have the preprocessed data, we apply few image augmentations, import pretrained resnet-18 model as encoder and train the UNet model. We use two evaluation metrics to assess the performance of our model on the dataset. First, the accuracy,
which is defined as the percentage of correctly classified pixels. Secondly, the intersection over union (IoU) of the positive (building) class, which is defined as the number of pixels labeled as building in both the prediction and the reference, divided by the number of pixels labeled as building in the prediction or the reference IOU and accuracy. For training the model we define a combined loss function which is summation of Dice-coefficient loss function and Crossentropy loss function.

#### Approach 1 : Resized to 512 and Resnet-34 as encoder
Our model got max accuracy of 95% but IOU of 50%, which did not cross the baseline model of INRIA mentioned here. It might be due to huge information loss while resizing the images.

#### Approach 2 : Sliding Window Patches of size 250 and Resnet-18 as encoder
For JPEG images, our model got max accuracy of 95% and IOU of 70%.

For TIFF images, our model got max accuracy of 96% and IOU of 72%. We are submitting the predictions on test images using later model for the challenge as of 20th May 2019..

#### Approach 3 : Sliding Window Patches of size 256 with overlap of 6pixels and Resnet-18 as encoder
For TIFF images, our model got max accuracy of 96% and IOU of 75.5%. We are submitting the predictions on test images using later model for the challenge as of 27th May 2019.

#### Summary
This is a summary of the three approaches on validation set:

| Approach        | Image Preprocessing           | Accuracy  | IOU |
| --------------- |:-----------------------:| -----:|------:|
| 1               | resized to 512X512 size | 95% |  50%     |
| 2               | Sliced to 250X250 size(no overlap)  |   96% | 72%   |
| 3               | Sliced to 256X256 size (with overlap)     |    96% |  75.5%  |  

#### Submitted results on test set

| Test | Tiles| IOU | Accuracy |
|-----:|-----:|-----:|-----:|
|Bellingham, WA |36| 69.42 | 96.95|
|Bloomington, IN | 36 | 68.06 | 96.94 |
|Innsbruck, Austria |36| 72.67 | 96.74 |
|San Francisco, CA |36| 68.78 | 89.81 |
|East Tyrol, Austria | 36| 76.51 | 97.89 |
| Total | 180| 70.36 | 95.67 |

#### Next steps 
Improve the results with fine tuning and try different architectures.
