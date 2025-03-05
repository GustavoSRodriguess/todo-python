import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './index.css'

// Configuração global do axios
import axios from 'axios'
axios.defaults.baseURL = 'http://localhost:5000/api/v1'

createApp(App)
    .use(store)
    .use(router)
    .mount('#app')