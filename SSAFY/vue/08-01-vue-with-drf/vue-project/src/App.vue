<template>
  <header>
    <nav v-if="store.isLogin">
      <div>
        <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink> |
        <form @submit.prevent="store.logOut">
          <input type="submit" value="logOut">
        </form>
      </div>
    </nav>
    <nav v-else>
      <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink> |
      <RouterLink :to="{ name: 'SignUpView' }">Signup</RouterLink> |
      <RouterLink :to="{ name: 'LogInView' }">Login</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
</script>

<style scoped>
</style>
