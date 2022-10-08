# Best Deep Learning Projects for Advanced Learners [2022 Updated]

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ZohebAbai/Deep-Learning-Projects/master)

![welcome](https://media0.giphy.com/media/xUPGGDNsLvqsBOhuU0/giphy.gif?cid=ecf05e47mxzkfopuw507aun32t74ggidrxflwrvb779i1874&rid=giphy.gif)

#### Using both Tensorflow and PyTorch Libraries

**Get a glimpse of how similar/different these libraries are:**
[Pytorch vs Tensorflow on MNIST dataset](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/Pytorch_vs_Tensorflow.ipynb)

**In each notebook, we shall train using free Google Colab resources and eventually deploy them as gradio/streamlit app (depending on projects).**

## Notebooks:

### Fundamentals
* **Tensorflow Fundamentals** [TF Tensors Basics](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/00_Tensorflow_Fundamentals.ipynb)
	- Constants and Variables
	- Compatibility with Numpy
	- Random Generators
	- Basic Operations
* **Pytorch Fundamentals** [PT Tensors Basics](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/00_Pytorch_Fundamentals.ipynb)
	- Tensor Basic
	- Interoperability with Numpy
	- Basic Operations
	- Regression Model Training with Custom Data on GPU

### Structured Data	
* **Regression** - [Custom TF Model on Medical Insurance Dataset](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/01_TF_Regression.ipynb)
	- Minimal EDA
	- k-Fold Cross Validation
	- L1 Regularizers
	- Gradio App

### Computer Vision
* **Image Classification** - [Custom TF Model on Cifar10 Dataset](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/02_TF_Image_Classification.ipynb)
	- Image Augmentation
	- LR Finder
	- One-Cycle LR Scheduler
	- GradCAM visualisation
	- Gradio App
* **Multi-Label Image Classification** - [TF Transfer Learning on Custom Dataset](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/03_TF_Multilabel_Image_Classification.ipynb)
	- Custom Dataset 
	- TF Record with Image Augmentation
	- Custom Loss Function
	- Transfer Learning
	- Performance Profiling
	- Gradio App
* **Image Generation** - [TF VAE Image Generation on Celeb Faces](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/04_TF_Image_Generation.ipynb)
	- Custom Architecture using Probabilistic Layers
	- Reduce LR on Plateau Scheduler
	- New Generated Faces
	- Reconstructing Faces
	- Feature Manipulation
	- Face Morphing
	- Visualize clusters on UMAP-reduced 1D latent vector
* **Metric Learning** - [TF Similarity Models on Dog-Cat Breed Dataset](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/05_TF_Metric_Learning.ipynb)
	- Tensorflow Similarity
	- Transfer Learning with an embedding layer and Multisimilarity loss
	- ANN Search: Indexing, Calibration, Querying 
	- Precision-Recall Curve
	- UMAP-reduced clustering with interactive visualization

* **Image Translation** - [TF Pix2Pix on Edges-to-Handbags Dataset](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/08_TF_Pix2Pix_on_Edges2Handbags.ipynb)
	- Understanding Pix2Pix Architecture
	- Training it from scratch with additional loss fucntion
	- Focal Frequency Loss
	- Using Tensorboard during model training
	- Image Generation

* **Image Segmentation** - [HF SegFormer on Road-Sidewalk Dataset](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/09_HF_Image_Segmentation_using_Transformers.ipynb)
	- Understanding Semantic Segmentation using Transformers
	- Fine-Tuning it using Huggingface Modules
	- Mean IOU metric
	- Publishing the model under open source licence
	- Model Inference 

* **Pose Estimation** - 
* **Object Detection** - 

### Natural Language Processing
* **Pre-Neural NLP** - [Heuristics-based & Statistical Methods in NLP](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/00_Pre_Neural_NLP.ipynb)
	- Basics of Sentiment Analysis
	- Valence Aware Dictionary and Sentiment Reasoner (VADER)
	- Support Vector Machines (SVM)
	- Grid Search for Hyperparameters
	- ROC Curve
* **Understanding Vanilla Transformers** - [Vanilla Transformers](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/06_Understanding_Vanilla_Transformers.ipynb)
	- Understanding Seq2Seq Models
	- Understanding Attention Mechanism
	- Understanding Transformer Architecture
* **Vanilla Transformer Comment to Code** - [PT Train Vanilla Transformer (Sequence to Sequence)](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/07_Vanilla_Transformer_Comment_to_Code.ipynb)
	- Dataset Augmentation
	- Custom Tokenizer
	- Build Complete Transformer Architecture 
	- Custom Loss
	- Display Attention
	- Gradio App

### Experimental (Excellent ML Applications of few yet not stable libraries)
* **JAX Basics** - [JAX Basics](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/JAX_Basics.ipynb)
	- Why JAX?
	- How randomness is handled
	- Speed Comparison
	- Asynchronous Dispatch
	- JIT Compilation
	- Auto-differentiation with grad
	- Auto-vectorization with Vmap
	- SPMD Programming with Pmap on TPU
	- Device Memory Profiler
    
* **PySyft - Secure and Privacy AI**
	- [Data Owner](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/Data_Owner.ipynb)
	- [Data Scientist](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/Data_Scientist.ipynb)
	- Differential Privacy
	- Remote Data Science
	- Covid-19 trends prediction

* **TenSeal - Homomorphic Encryption on Tensors**
	- [Homomorphic Encryption Basic and Encrypted Inference](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/HE_Basics_n_Inference.ipynb)
	- [Homomorphic Encryption NN Training](https://nbviewer.org/github/ZohebAbai/Deep-Learning-Projects/blob/master/HE_Training.ipynb)
	- Tenseal Context
	- Basic Mathematical Operations on Encrypted Tensors
	- Encrypted Evaluation on Encrypted Test Data
	- Training Encrypted NN on Encrypted Data 


