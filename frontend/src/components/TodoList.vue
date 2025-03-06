<template>
  <div class="todo-container text-yellow-500">
    <!-- Formulário para adicionar tarefas -->
    <div class="card mb-6 bg-gray-800 drop-shadow-2xl border border-gray-600">
      <h2 class="text-xl font-bold mb-4">Nova Tarefa</h2>
      <form @submit.prevent="addTodo">
        <div class="mb-4">
          <label for="title" class="block text-sm font-medium text-yellow-500 mb-1">Título</label>
          <input 
            type="text" 
            id="title" 
            v-model="newTodo.title" 
            class="input-field border border-gray-500 focus:outline-2 focus:outline-offset-2 focus:outline-violet-500"
            placeholder="O que você precisa fazer?"
            required
          >
        </div>
        
        <div class="mb-4">
          <label for="description" class="block text-sm font-medium text-yellow-500 mb-1">Descrição</label>
          <textarea 
            id="description" 
            v-model="newTodo.description" 
            class="input-field border border-gray-500"
            placeholder="Detalhes da tarefa (opcional)"
            rows="3"
          ></textarea>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
          <div>
            <label for="priority" class="block text-sm font-medium text-yellow-500 mb-1">Prioridade</label>
            <select id="priority" v-model="newTodo.priority" class="input-field border border-gray-500">
              <option value="1">Baixa</option>
              <option value="2">Média</option>
              <option value="3">Alta</option>
            </select>
          </div>
          
          <div>
            <label for="due_date" class="block text-sm font-medium text-yellow-500 mb-1">Data Limite</label>
            <input 
              type="date" 
              id="due_date" 
              v-model="newTodo.due_date" 
              class="input-field border border-gray-500 focus:outline-2 focus:outline-offset-2 focus:outline-violet-500"
            >
          </div>
        </div>
        
        <div class="flex justify-end">
          <button type="submit" class="btn btn-secondary">Adicionar Tarefa</button>
        </div>
      </form>
    </div>
    
    <!-- Filtros -->
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-2xl font-bold">Minhas Tarefas</h2>
      
      <div class="flex space-x-2">
        <button 
          @click="filter = 'all'" 
          class="px-3 py-1 rounded-md"
          :class="filter === 'all' ? 'bg-yellow-500 text-white' : ''"
        >
          Todas
        </button>
        <button 
          @click="filter = 'active'" 
          class="px-3 py-1 rounded-md"
          :class="filter === 'active' ? 'bg-yellow-500 text-white' : ''"
        >
          Pendentes
        </button>
        <button 
          @click="filter = 'completed'" 
          class="px-3 py-1 rounded-md"
          :class="filter === 'completed' ? 'bg-yellow-500 text-white' : ''"
        >
          Concluídas
        </button>
      </div>
    </div>
    
    <!-- Lista de tarefas -->
    <div v-if="loading" class="flex justify-center my-8">
      <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary"></div>
    </div>
    
    <div v-else-if="filteredTodos.length === 0" class="card my-4 text-center py-8 bg-gray-600">
      <p class="text-gray-800">Nenhuma tarefa encontrada</p>
    </div>
    
    <div v-else class="space-y-4">
      <div 
        v-for="todo in filteredTodos" 
        :key="todo.id" 
        class="card transition-all duration-200"
        :class="{
          'border-l-4 border-red-500': todo.priority === 3,
          'border-l-4 border-yellow-500': todo.priority === 2,
          'border-l-4 border-blue-500': todo.priority === 1,
          'opacity-75': todo.completed
        }"
      >
        <div class="flex items-start">
          <input 
            type="checkbox" 
            :checked="todo.completed" 
            @change="toggleTodo(todo)"
            class="mt-1 h-5 w-5 text-primary rounded focus:ring-primary"
          >
          
          <div class="ml-3 flex-1">
            <div class="flex justify-between">
              <h3 
                class="text-lg font-semibold"
                :class="{'line-through text-gray-500': todo.completed}"
              >
                {{ todo.title }}
              </h3>
              
              <div class="flex space-x-2">
                <button 
                  @click="editTodo(todo)" 
                  class="text-gray-500 hover:text-primary"
                >
                  <span class="sr-only">Editar</span>
                  <i class="fas fa-edit"></i>
                </button>
                
                <button 
                  @click="deleteTodo(todo)" 
                  class="text-gray-500 hover:text-red-500"
                >
                  <span class="sr-only">Excluir</span>
                  <i class="fas fa-trash"></i>
                </button>
              </div>
            </div>
            
            <p 
              v-if="todo.description" 
              class="text-yellow-500 mt-1"
              :class="{'text-gray-400': todo.completed}"
            >
              {{ todo.description }}
            </p>
            
            <div class="mt-2 flex flex-wrap gap-2">
              <span 
                v-if="todo.due_date" 
                class="inline-flex items-center text-xs px-2 py-1 rounded-full"
                :class="isOverdue(todo) ? 'bg-red-100 text-red-800' : 'bg-blue-100 text-blue-800'"
              >
                <i class="fas fa-calendar-alt mr-1"></i>
                {{ formatDate(todo.due_date) }}
              </span>
              
              <span class="inline-flex items-center text-xs px-2 py-1 rounded-full"
                :class="{
                  'bg-red-100 text-red-800': todo.priority === 3, 
                  'bg-yellow-100 text-yellow-800': todo.priority === 2, 
                  'bg-blue-100 text-blue-800': todo.priority === 1
                }"
              >
                <i class="fas fa-flag mr-1"></i>
                {{ priorityText(todo.priority) }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Modal de edição -->
    <div v-if="editingTodo" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-lg shadow-xl max-w-2xl w-full p-6">
        <h2 class="text-xl font-bold mb-4">Editar Tarefa</h2>
        
        <form @submit.prevent="updateTodo">
          <div class="mb-4">
            <label for="edit-title" class="block text-sm font-medium text-yellow-500 mb-1">Título</label>
            <input 
              type="text" 
              id="edit-title" 
              v-model="editingTodo.title" 
              class="input-field"
              required
            >
          </div>
          
          <div class="mb-4">
            <label for="edit-description" class="block text-sm font-medium text-yellow-500 mb-1">Descrição</label>
            <textarea 
              id="edit-description" 
              v-model="editingTodo.description" 
              class="input-field"
              rows="3"
            ></textarea>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div>
              <label for="edit-priority" class="block text-sm font-medium text-yellow-500 mb-1">Prioridade</label>
              <select id="edit-priority" v-model="editingTodo.priority" class="input-field">
                <option value="1">Baixa</option>
                <option value="2">Média</option>
                <option value="3">Alta</option>
              </select>
            </div>
            
            <div>
              <label for="edit-due_date" class="block text-sm font-medium text-yellow-500 mb-1">Data Limite</label>
              <input 
                type="date" 
                id="edit-due_date" 
                v-model="editingTodo.due_date" 
                class="input-field"
              >
            </div>
          </div>
          
          <div class="flex justify-end space-x-3">
            <button 
              type="button" 
              @click="cancelEdit" 
              class="btn bg-gray-200 hover:bg-gray-300 text-gray-800"
            >
              Cancelar
            </button>
            <button type="submit" class="btn btn-primary">Salvar Alterações</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, computed, onMounted } from 'vue';

export default {
  name: 'TodoList',
  
  setup() {
    // Estado
    const todos = ref([]);
    const loading = ref(true);
    const filter = ref('all');
    const editingTodo = ref(null);
    
    const newTodo = ref({
      title: '',
      description: '',
      priority: 1,
      due_date: null,
      completed: false
    });
    
    // Métodos para manipulação de dados
    const fetchTodos = async () => {
      loading.value = true;
      try {
        const response = await axios.get('/todos');
        todos.value = response.data;
      } catch (error) {
        console.error('Erro ao buscar tarefas:', error);
      } finally {
        loading.value = false;
      }
    };
    
    const addTodo = async () => {
      try {
        const todoData = { ...newTodo.value };
        
        // Converter prioridade para número
        todoData.priority = Number(todoData.priority);
        
        const response = await axios.post('/todos', todoData);
        todos.value.push(response.data);
        
        // Limpar formulário
        newTodo.value = {
          title: '',
          description: '',
          priority: 1,
          due_date: null,
          completed: false
        };
      } catch (error) {
        console.error('Erro ao adicionar tarefa:', error);
      }
    };
    
    const toggleTodo = async (todo) => {
      try {
        const response = await axios.patch(`/todos/${todo.id}/toggle`);
        const index = todos.value.findIndex(t => t.id === todo.id);
        if (index !== -1) {
          todos.value[index] = response.data;
        }
      } catch (error) {
        console.error('Erro ao alternar status da tarefa:', error);
      }
    };
    
    const deleteTodo = async (todo) => {
      if (!confirm('Tem certeza que deseja excluir esta tarefa?')) return;
      
      try {
        await axios.delete(`/todos/${todo.id}`);
        todos.value = todos.value.filter(t => t.id !== todo.id);
      } catch (error) {
        console.error('Erro ao excluir tarefa:', error);
      }
    };
    
    const editTodo = (todo) => {
      // Clonar o objeto para não modificar diretamente o original
      editingTodo.value = JSON.parse(JSON.stringify(todo));
      
      // Formatar a data para o input type="date"
      if (editingTodo.value.due_date) {
        editingTodo.value.due_date = editingTodo.value.due_date.split('T')[0];
      }
    };
    
    const updateTodo = async () => {
      try {
        const todoData = { ...editingTodo.value };
        
        // Converter prioridade para número
        todoData.priority = Number(todoData.priority);
        
        const response = await axios.put(`/todos/${todoData.id}`, todoData);
        
        const index = todos.value.findIndex(t => t.id === todoData.id);
        if (index !== -1) {
          todos.value[index] = response.data;
        }
        
        // Fechar modal
        cancelEdit();
      } catch (error) {
        console.error('Erro ao atualizar tarefa:', error);
      }
    };
    
    const cancelEdit = () => {
      editingTodo.value = null;
    };
    
    // Funções utilitárias
    const formatDate = (dateString) => {
      const date = new Date(dateString);
      return date.toLocaleDateString();
    };
    
    const isOverdue = (todo) => {
      if (!todo.due_date || todo.completed) return false;
      
      const dueDate = new Date(todo.due_date);
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      
      return dueDate < today;
    };
    
    const priorityText = (priority) => {
      switch (Number(priority)) {
        case 1: return 'Baixa';
        case 2: return 'Média';
        case 3: return 'Alta';
        default: return 'Normal';
      }
    };
    
    // Dados filtrados
    const filteredTodos = computed(() => {
      if (filter.value === 'all') return todos.value;
      if (filter.value === 'active') return todos.value.filter(todo => !todo.completed);
      if (filter.value === 'completed') return todos.value.filter(todo => todo.completed);
      return todos.value;
    });
    
    // Inicialização
    onMounted(() => {
      fetchTodos();
    });
    
    return {
      todos,
      loading,
      filter,
      newTodo,
      editingTodo,
      filteredTodos,
      fetchTodos,
      addTodo,
      toggleTodo,
      deleteTodo,
      editTodo,
      updateTodo,
      cancelEdit,
      formatDate,
      isOverdue,
      priorityText
    };
  }
};
</script>