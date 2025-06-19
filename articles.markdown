---
layout: default
title: 文章栏目
---

# 文章栏目

<div class="articles-container">
{% for post in site.posts %}
  <article class="article-card">
    <h2 class="article-title"><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p class="article-date">{{ post.date | date: "%Y年%m月%d日" }}</p>
    <div class="article-excerpt">{{ post.excerpt }}</div>
    <a href="{{ post.url }}" class="read-more-btn">阅读全文 →</a>
  </article>
{% endfor %}
</div>