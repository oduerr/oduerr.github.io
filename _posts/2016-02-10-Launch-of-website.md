---
layout: post
title: "Finally I got a website"
---

Finally, I found some time putting a first website together. It uses [Jekyll](http://jekyllrb.com) and one can use markdown to author the posts and all the pages. I basically followed the instruction given at: [http://jmcglone.com/guides/github-pages/](http://jmcglone.com/guides/github-pages/)

Some things I did not find straight forward.

## Preview the website before commiting to github. 
In the root directory of the project `oduerr.github.io` do:

```
  jekyll serve
```

## Using markdown not only in the posts
If you want to use markdown, simply use the extension `md` instead of the `html` file: the magic happens in the background.

## Using Latex like formulas
If you want to use formulas in your page you have to include
```
  		<script type="text/javascript"
        src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
      </script>
```
<p>
in the `_layouts/default.html` file. Then you can do cool things like
$$
 \hat{H} |\,\psi (t) \rangle = - \frac{\hbar}{\mathrm{i}}\frac{\partial}{\partial t} |\,\psi (t) \rangle 
$$


