---
layout: default
title: Research Interest
---


# Research Interest
<div style="text-align: right;">
    <img src="../imgs/Oliver_Elvis.jpg" alt="image" style="float: right;" width="250" class="profile-photo">
</div>
My research primarily explores the synergy between **deep learning** and **statistics**, focusing on three main areas:


## 1) Deep Learning for Modeling Uncertainty:
 In complex systems, like weather forecasting, predictions are inherently uncertain. In deep learning, this uncertainty, known as aleatoric uncertainty, is captured by outputting probability distributions instead of single values. We contribute to this field by developing [deep transformation models](https://scholar.google.ch/citations?view_op=view_citation&hl=de&user=T8hH3TMnFPwC&sortby=pubdate&citation_for_view=T8hH3TMnFPwC:mB3voiENLucC) allowing flexible output distributions and extended the method to include [interpretable traditional statistical regression models](https://www.sciencedirect.com/science/article/abs/pii/S003132032100443X). We applied these models to practical problems like predicting the [day ahead power consumption](https://ieeexplore.ieee.org/abstract/document/10066318) or to[medical applications](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.202100379). 

## 2) Quantifying Uncertainty in Deep Learning Models:
Recently, deep neural networks have become standard in many areas. However, they can be spectacularly wrong. 
Consider the case where a network should classify an image of a class it has never seen before. Technically speaking, the image class is outside the training set. This is shown in the following picture, where a network trained on dogs is shown a cat. 
<img src="../imgs/Rapid_Fire_Presentation_v2.jpg" alt="Rapid Fire Presentation" width="400" style="float:left;">  The network overconfidently assigns a high probability to the wrong class. I get scared when I think of self-driving cars being overconfident. This kind of uncertainty is also referred to as epistemic uncertainty. Standard networks cannot state the uncertainty of a prediction. Bayesian Statistics would be a perfect framework to include this kind of uncertainty. However, they are computationally expensive, so approximations are very important. To overcome this challenge, we have contributed to the field by developing novel approaches such as variational inference models for flexible posterior distributions ([Bernstein Flows for Flexible Posteriors in Variational Bayes](https://arxiv.org/abs/2202.05650)), even faster approximations to existing Bayesian approximations ([single shot dropout](https://arxiv.org/abs/2308.12785)), more efficient approximations such as single-shot dropout, and subspace inference methods enabling MCMC sampling in low-dimensional proxy spaces within the vast network parameter space ([Bayesian Semi-structured Subspace Inference](https://scholar.google.ch/citations?view_op=view_citation&hl=de&user=T8hH3TMnFPwC&sortby=pubdate&citation_for_view=T8hH3TMnFPwC:D03iK_w7-QYC)). We applied these methods in various fields to develop to practical applications. In high content screening [robust deep learning approach in the presence of unknown phenotypes](https://www.liebertpub.com/doi/10.1089/adt.2018.859), medical applications ([Deep transformation models for functional outcome prediction after acute ischemic stroke](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.202100379) and [Integrating uncertainty in deep neural networks for MRI based stroke analysis](https://www.sciencedirect.com/science/article/abs/pii/S1361841520301547)). 

## 3) Merging Deep Learning with Statistical Models: 
While deep learning is exceptional in identifying complex patterns, statistical models offer superior interpretability. Our research aims to merge these two worlds, creating models that are both powerful and understandable. This approach is evident in most of our published works, where we seamlessly integrate deep learning with statistical insights.



<!-- ## Book on probabilistic deep learning
To foster the wider application of these methods, we also wrote a [book on probabilistic deep learning](https://www.manning.com/books/probabilistic-deep-learning-with-python). The book is a practical guide to the application of probabilistic deep learning models. The notebooks are freely available [here](https://tensorchiefs.github.io/dl_book/).

<div style="text-align: left;">
    <img src="imgs/probabilistic.png" alt="Probabilistic Image" style="left;" height="200">
</div>  -->
