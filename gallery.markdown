---
layout: default
title: 画廊
---

# 我的画廊

这里展示我的摄影作品和生活瞬间。

<div class="gallery-container">
  <img src="/assets/images/00014-people.jpg" alt="人物摄影" class="gallery-img" />
  <img src="/assets/images/00011-city.jpg" alt="城市风光" class="gallery-img" />
  <img src="/assets/images/00019-art.jpg" alt="艺术作品" class="gallery-img" />
  <img src="/assets/images/00013-macro.jpg" alt="微距摄影" class="gallery-img" />
  <img src="/assets/images/00016-city.jpg" alt="城市风光" class="gallery-img" />
  <img src="/assets/images/00015-nature.jpg" alt="自然风光" class="gallery-img" />
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