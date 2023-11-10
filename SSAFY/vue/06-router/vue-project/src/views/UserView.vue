<template>
    <div>
        <h1>UserView</h1>
        <h2>{{ $route.params.id }} 유저의 페이지입니다.</h2>
        <h2>{{ userId }} 유저의 페이지입니다.</h2>
        <button @click="goHome">홈으로</button>
        <button @click="goAnotherUser">100번 유저 페이지</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
const goHome = function() {
    // router.push({name: 'home'})
    router.replace({name: 'home'})
}
// In-component Guard

// 1. onBeforeRouteLeave
onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('가든가 말든가')
    if (answer === false) {
        return false
    }
})
// 2. onBeforeRouteUpdate
const goAnotherUser = function () {
    router.push({ name: 'user', params: { id: 100 }})
}
onBeforeRouteUpdate((to, from) => {
    userId.value = to.params.id
})
</script>

<style scoped>

</style>