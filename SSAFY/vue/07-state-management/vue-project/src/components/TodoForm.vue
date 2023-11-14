<template>
    <div>
        <form @submit.prevent="createTodo(todoText)" ref="formElem">
            <input type="text" v-model="todoText">
            <input type="submit">

        </form>
    </div>
</template>

<script setup>
import { sayT1, sayDongHyeon } from '@/utils/dongHyeon.js'
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

const todoText = ref('')
const store = useCounterStore()
const formElem = ref(null)
const createTodo = function () {
    store.addTodo(todoText)
    formElem.value.reset()
}
sayT1()
</script>

<style scoped>

</style>