---
layout: default
title: 画廊
---

# 我的画廊

这里展示我的摄影作品和生活瞬间。

<div class="gallery-container">
  <img src="/assets/images/00011-nature.jpg" alt="自然风光" class="gallery-img" />
  <img src="/assets/images/00012-nature.jpg" alt="自然风光" class="gallery-img" />
  <img src="/assets/images/00013-animal.jpg" alt="动物" class="gallery-img" />
  <img src="/assets/images/00014-music.jpg" alt="音乐" class="gallery-img" />
  <img src="/assets/images/00016-food.jpg" alt="食物" class="gallery-img" />
  <img src="/assets/images/00017-fashion.jpg" alt="时尚" class="gallery-img" />
  <img src="/assets/images/00018-animal.jpg" alt="动物" class="gallery-img" />
  <img src="/assets/images/00019-education.jpg" alt="教育" class="gallery-img" />
</div>

<style>
  .modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.9);
  }
  
  .modal-content {
    display: block;
    max-width: 90%;
    max-height: 90%;
    margin: auto;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  
  .close {
    position: absolute;
    top: 15px;
    right: 35px;
    color: #f1f1f1;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
  }
</style>

<div id="imageModal" class="modal">
  <span class="close">&times;</span>
  <img class="modal-content" id="modalImage">
</div>

<script>
  const modal = document.getElementById('imageModal');
  const modalImg = document.getElementById('modalImage');
  const closeBtn = document.querySelector('.close');
  
  document.querySelectorAll('.gallery-img').forEach(img => {
    img.addEventListener('click', function() {
      modal.style.display = 'block';
      modalImg.src = this.src;
    });
  });
  
  closeBtn.addEventListener('click', function() {
    modal.style.display = 'none';
  });
  
  window.addEventListener('click', function(event) {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });
</script>