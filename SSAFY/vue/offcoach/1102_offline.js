

const { createApp, ref, computed } = Vue;

const app = createApp({
    setup () {
        // 할 일 목록
        const todos = ref([])
        // 사용자의 입력을 받을 변수
        const newTodo = ref('')
        // 새로운 할 일을 추가하는 메서드
        let todoId = 1;

        const addTodo = () => {
            const tmp = {
                id: todoId ++,
                text: newTodo.value,
                completed: false,
            }
            todos.value.push(tmp)
            newTodo.value = '' // 입력 필드 초기화
        }
        const deleteTodo = (index) => {
            todos.value.splice(index, 1)
        }
        const toggleTodoStatus = (todo) => {
            todo.completed = !todo.completed
        }
        const deleteCompletedTodos = () => {
            todos.value = todos.value.filter((todo) => {
                return !todo.completed
            })
        }
        const todoCount = computed(() => {
            return todos.value.filter((todo) => todo.completed).length > 0
        })
        
        return {
            todos,
            newTodo,
            addTodo,
            deleteTodo,
            toggleTodoStatus,
            deleteCompletedTodos,
            todoCount,
        }
    }
})
app.mount('#app')