---
layout: post
title: Simple cosmicfishpie example
date: 2023-11-11 08:57:00-0400
description: A cosmology calculator from CosmicFishPie
tags: formatting jupyter
categories: cosmology
giscus_comments: true
related_posts: false
---

{::nomarkdown}
{% assign jupyter_path = "assets/jupyter/Cosmology-Calculator.ipynb" | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/Cosmology-Calculator.ipynb %}{% endcapture %}
{% if notebook_exists == "true" %}
{% jupyter_notebook jupyter_path %}
{% else %}

<p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}

Note that the jupyter notebook supports both light and dark themes.
