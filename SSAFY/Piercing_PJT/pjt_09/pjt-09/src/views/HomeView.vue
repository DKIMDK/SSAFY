<template>

  <h1>메인</h1>
  <div>
    <input v-model="keyword">
    <button @click="submit()" type="submit">검색</button>
    <hr>
    <h2>검색 결과</h2>

    <div v-for="video in videos" :key="video.id">
      <img :src="video.snippet.thumbnails.medium.url" alt="img">
      <p @click="goDetail(video)">{{ video.snippet.title }}</p>
      <p>{{ video.snippet.channelTitle }}</p>
      
    </div>
  </div>
    


</template>
<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const APIKEY = "AIzaSyCq69jA_SSoun6sAwHuLgVye5mVGxcs_SY"
const keyword = ref('')
const videos = ref([])
const router = useRouter()
const URL = computed(() => {
  return `https://www.googleapis.com/youtube/v3/search?&key=${APIKEY}&part=snippet&type=video&q=${keyword.value}`
})
const submit = function () {
  
  axios.get(URL.value)
  .then((response) => {
    console.log(response.data.items)
    videos.value = response.data.items
  }).catch((error) => {
    console.error(error)
  })
}

const goDetail = function (video) {
  router.push(`/${video.snippet.id}`)
}        

</script>

