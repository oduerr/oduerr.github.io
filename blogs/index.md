---
layout: default
title: "Blogs and Talks"
author: "Oliver Dürr"
---
# Recent Talks

(March 2023) [KI im Jahre 2023](https://oduerr.github.io/talks/ki_2023.html)

# Older Talks
Talks I gave at the brownbag seminars in [Winterthur](https://tensorchiefs.github.io/bbs/) in [Konstanz](https://ioskn.github.io/bbs/). 
[Older talks](https://github.com/oduerr/blogs/old_talks.html).


<h2>{{ page.title }}</h2>

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> » <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
