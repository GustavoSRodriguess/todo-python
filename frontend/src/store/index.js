import { createStore } from 'vuex'

export default createStore({
    state: {
        todos: []
    },
    getters: {
        allTodos: state => state.todos,
        activeTodos: state => state.todos.filter(todo => !todo.completed),
        completedTodos: state => state.todos.filter(todo => todo.completed)
    },
    mutations: {
        SET_TODOS(state, todos) {
            state.todos = todos
        },
        ADD_TODO(state, todo) {
            state.todos.push(todo)
        },
        UPDATE_TODO(state, updatedTodo) {
            const index = state.todos.findIndex(todo => todo.id === updatedTodo.id)
            if (index !== -1) {
                state.todos.splice(index, 1, updatedTodo)
            }
        },
        REMOVE_TODO(state, id) {
            state.todos = state.todos.filter(todo => todo.id !== id)
        }
    },
    actions: {
        fetchTodos({ commit }) {
            // Aqui você pode implementar chamadas à API
            // Por enquanto, usaremos dados locais nos componentes
        },
        addTodo({ commit }, todo) {
            commit('ADD_TODO', todo)
        },
        updateTodo({ commit }, todo) {
            commit('UPDATE_TODO', todo)
        },
        removeTodo({ commit }, id) {
            commit('REMOVE_TODO', id)
        }
    }
})