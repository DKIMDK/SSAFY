<template>
	<div>
		{{ myMsg }}
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild
     :my-msg="myMsg" 
     :dynamic-props="name"
     @update-name="updateName"
     />
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가인자전달</button>
    <!-- <button @click="updateName">이름변경</button> -->
</div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'


// defineProps({
// 	myMsg: {
// 		type: String,
// 		required: true,
// 	}
// })

// props 데이터를 script에서 사용하려면
const props = defineProps({
  myMsg: {
    type: String,
    required: true,
  },
  dynamicProps: String,
})
// emit 선언 방식
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const buttonClick = function () {
  emit('someEvent')
}

const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}
console.log(props)
console.log(props.myMsg)


</script>

<style scoped>

</style>