<template>
    <main>
      <h1>동영상 상세 정보</h1>
      <div>
      <img :src="video.snippet.thumbnails.medium.url" alt="img">
      <p>{{ video.snippet.title }}</p>
      <p>{{ video.snippet.channelTitle }}</p>
      </div>
    </main>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const APIKEY = "AIzaSyCq69jA_SSoun6sAwHuLgVye5mVGxcs_SY"
const video = ref('')
const route = useRoute()

onMounted(async () => {
  const videoId = route.params.snippet.id
  const response = await axios.get(`https://www.googleapis.com/youtube/v3/videos?key=${APIKEY}&part=snippet&id=${videoId}`)
  video.value = response.data.items[0]
})
const URL = computed(() => {
  return `https://www.googleapis.com/youtube/v3/search?&key=${APIKEY}&part=snippet&type=video&q=${keyword.value}`
})
const submit = function () {
  
  axios.get(URL.value)
  .then((response) => {
    console.log(response.data.items)
    video.value = response.data.items
  }).catch((error) => {
    console.error(error)
  })
}

  </script>
  
  