## Assigning uncertainty in deep learning

Recently deep neural networks have become standard in many areas of analysing perception data like images or audio. However, they can be spectacular wrong. E.g. consider the case, where a network should classify an image of a class it never saw before. Technically speaking the image class is not in training set. This is shown in the following picture, where a network trained on dogs is shown a cat. 

![imgs/Rapid_Fire_Presentation_v2.jpg](imgs/Rapid_Fire_Presentation_v2.jpg)      

The network overconfidently assigns a high probability to the wrong class. I get scared when I think of self driving cars being overconfident. While standard networks cannot state their uncertainty of a prediction, novel methods allow to include uncertainty information. One way to do so is to use dropout also during test time. [Yarin Gal has shown that this allows to quantify uncertainty in his Phd thesis](https://arxiv.org/abs/1506.02142).

We use this approach in several places:

* For the use in high content screening see: [Oliver Dürr, Elvis Murina, Daniel Siegismund, Vasily Tolkachev, Stephan Steigele, and Beate Sick. "Know When You Don't Know: A Robust Deep Learning Approach in the Presence of Unknown Phenotypes" ASSAY and Drug Development Technologies.](https://www.liebertpub.com/doi/10.1089/adt.2018.859)

And in other ongoing projects, stay tuned.


