<template>
  <div>
    <h1>Login Page</h1>
    <form @submit.prevent="logIn">
      <input type="text" v-model.trim="username"><br>
      <input type="password" v-model.trim="password"><br>
      <input type="submit" value="login">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style>

</style>
