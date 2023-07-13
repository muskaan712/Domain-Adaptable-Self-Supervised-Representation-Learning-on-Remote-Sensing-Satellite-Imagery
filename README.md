# Title

Domain Adaptable Self-supervised Representation Learning on Remote Sensing Satellite Imagery

# Venue

Accepted in International Joint Conference on Neural Networks (IJCNN) 2023


# Article

[Arxiv Version]()

# Recorded Presentation
[![IMAGE ALT TEXT HERE](https://github.com/muskaan712/Domain-Adaptable-Self-Supervised-Representation-Learning-on-Remote-Sensing-Satellite-Imagery/blob/main/figures/sih_thumbnail.PNG)](https://www.youtube.com/watch?v=NOjXK1_cdhA)


# Abstract

This work presents a novel self-supervised pre-training method to learn efficient representations without labels on histopathology medical images utilizing magnification factors. Other state-of-the-art works mainly focus on fully supervised learning approaches that rely heavily on human annotations. However, the scarcity of labeled and unlabeled data is a long-standing challenge in histopathology. Currently, representation learning without labels remains unexplored in the histopathology domain. The proposed method, Magnification Prior Contrastive Similarity (MPCS), enables self-supervised learning of representations without labels on small-scale breast cancer dataset BreakHis by exploiting magnification factor, inductive transfer, and reducing human prior. The proposed method matches fully supervised learning state-of-the-art performance in malignancy classification when only 20% of labels are used in fine-tuning and outperform previous works in fully supervised learning settings for three public breast cancer datasets, including BreakHis. Further, It provides initial support for a hypothesis that reducing human-prior leads to efficient representation learning in self-supervision, which will need further investigation.

# Domain Adaptation by Self-supervised Representation Learning Method
[SimCLR](http://proceedings.mlr.press/v119/chen20j.html) contrastive learning method employed for self-supervised representation learning part.
<p align="center">
  <img src="https://github.com/muskaan712/Domain-adaptable-self-supervised-representation-learning-based-classification-of-remotely-sensed-sat/blob/main/figures/contrastive_ssl_on_remote_sensing.PNG">
</p>

Domain Adaptation Framework

<p align="center">
  <img src="https://github.com/muskaan712/Domain-adaptable-self-supervised-representation-learning-based-classification-of-remotely-sensed-sat/blob/main/figures/ssl_domain_adpation_framework.PNG">
</p>


# Datasets
Three publically available datasets from remote sensing domain are chosen for exprimentations.

1. [SIRI-WHU Dataset](http://www.lmars.whu.edu.cn/prof_web/zhongyanfei/e-code.html) - The SIRI-WHU dataset for classification has 2400 photos sorted into 12 classifications. This dataset was obtained from Google Earth and mainly included metropolitan regions in China, with the image collection developed by Wuhan University's RS IDEA Group (SIRI-WHU). It consists of 12 classes: Agriculture, Commercial, Harbor, Idle land, Industrial, Meadow, Overpass, Park, Pond, Residential, River, and Water. Each class comprises 200 pictures that are 200 x 200 pixels in size.
2. [UC Merced Dataset](http://weegee.vision.ucmerced.edu/datasets/landuse.html) - The image data in the UC Merced dataset were manually extracted from large-sized images in the United States Geological Survey (USGS) National Map Urban Area Imagery collection for numerous cities across the country (United States). This big ground truth picture collection consists of 21 land-use types, each with 100 pictures. The 21 classes were namely agricultural, airplane, baseball diamond, beach, buildings, chaparral, dense residential, forest, freeway, golf course, harbor, intersection, medium residential, mobile home park, overpass, parking lot, river, runway, sparse residential, storage tanks, and tennis court. This public domain imagery has a pixel resolution of 1 foot, with each image being 256x256 pixels.
3. [MLRSNet Dataset](https://data.mendeley.com/datasets/7j9bv9vwsx/2) - MLRSNet offers several satellite-based perspectives of the world. It comprises optical satellite images with great spatial resolution—between 1,500 and 3,000 example photos in every 46 categories in the 109,161 remote sensing photographs makeup MLRSNet. The photos are 256256 pixels and have different pixel sizes (10m to 0.1m). The dataset can be used for picture segmentation, image retrieval, and classification based on multiple labels.

# Model Weights
 
1. [SSL Pretrained Model on SIRI-WHU Dataset](https://github.com/muskaan712/Domain-adaptable-self-supervised-representation-learning-based-classification-of-remotely-sensed-sat/tree/main/Pretext_Checkpoints/SIRI-WHU)
2. [SSL Pretrained Model on UC Merced Dataset](https://github.com/muskaan712/Domain-adaptable-self-supervised-representation-learning-based-classification-of-remotely-sensed-sat/tree/main/Pretext_Checkpoints/UCMD)
2. [SSL Pretrained Model on MLRSNet Dataset](https://github.com/muskaan712/Domain-adaptable-self-supervised-representation-learning-based-classification-of-remotely-sensed-sat/tree/main/Pretext_Checkpoints/MLRSNet)

# Results
All the expriments have batch size of 256 and ResNet50 encoder.
<p align="center">
  <img src="https://github.com/muskaan712/Domain-adaptable-self-supervised-representation-learning-based-classification-of-remotely-sensed-sat/blob/main/results/SIRI-WHU_results.PNG">
</p>

<p align="center">
  <img src="https://github.com/muskaan712/Domain-adaptable-self-supervised-representation-learning-based-classification-of-remotely-sensed-sat/blob/main/results/MLRSNet_results.PNG">
</p>

<p align="center">
  <img src="https://github.com/muskaan712/Domain-adaptable-self-supervised-representation-learning-based-classification-of-remotely-sensed-sat/blob/main/results/UCMD_results.PNG">
</p>

# Qualitative
<p align="center">
  <img  src="https://github.com/muskaan712/Domain-adaptable-self-supervised-representation-learning-based-classification-of-remotely-sensed-sat/blob/main/results/activationmaps.PNG">
</p>


  
# Commands

1. Pretrain

``````

2. Finetune - downstream task

``````
