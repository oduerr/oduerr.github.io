---
layout: default
title: "Blogs and Talks"
author: "Oliver Dürr"
---
# Recent Talks

(March 2023) [KI im Jahre 2023](https://oduerr.github.io/talks/ki_2023.html)
(March 2023) [Neural network-based transformation models for prediction and inference](https://www.dropbox.com/s/jf0gxpmm99fuucx/kneib_OD_BS.pdf?dl=0)

# Older Talks
Talks I gave at the brownbag seminars in [Winterthur](https://tensorchiefs.github.io/bbs/) in [Konstanz](https://ioskn.github.io/bbs/). 
[Older talks](https://github.com/oduerr/blogs/old_talks.html).

# A somewhat random collection of post like documents 

<h3>Older</h3>
<small>
  <ul class="posts">
    {% for post in site.posts %}
      <li><span>{{ post.date | date_to_string }}</span> » <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
</small>
