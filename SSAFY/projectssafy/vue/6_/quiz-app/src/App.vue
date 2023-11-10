<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
<div class="container card text-center">
  <div class="card-header text-white bg-warning">
    Quiz 퀴즈
  </div>
  <div class="card-body">
    
    <p class="card-text">여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
  </div>
  <ul class="nav text-white bg-black justify-content-center">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled" aria-disabled="true">Disabled</a>
  </li>
</ul>
</div>
 
 <div>
  <h4>퀴즈 앱 사용방법</h4>
 </div>
</template>

<style scoped>
.header {
  background-color: #F1F1F1;
  text-align: center;
  padding: 20px;
}

.container {
  width:500px;
  height:200px;
}
</style>
