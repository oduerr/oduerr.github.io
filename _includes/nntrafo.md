## Neural Transformation Models
A valuable way to describe a probability distribution is by considering it as a transformation from a basic distribution to a more intricate one. Collaborating with Beate Sick and other colleagues, we employ networks to manage the transformation parameters. 

<div style="text-align: left;">
This concept can be implemented in various ways.
<img src="imgs/trafo.png" alt="image"  style="left;" width="400"><br>
 
* To create a versatile output distribution for a neural network (NN):
    * We introced this concept [in](https://ieeexplore.ieee.org/abstract/document/9413177/) using it to predict $p(age | image)$, the age of a person based on an image. 
    * To model the [power consumption forecasted by a neural network](https://ieeexplore.ieee.org/abstract/document/10066318))

* For comprehensible integration of NN and interpretable coefficients:
   *  For [ordinal outcomes](https://www.sciencedirect.com/science/article/abs/pii/S003132032100443X)
   *  For [functional outcome prediction after acute ischemic stroke](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.202100379)

* To model flexible distibitions for [variational inference](https://arxiv.org/abs/2202.05650)
</div>
