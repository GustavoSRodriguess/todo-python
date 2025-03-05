import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        // Carregamento lazy para melhor performance
        component: () => import('../views/AboutView.vue')
    }
]

const router = createRouter({
    history: createWebHistory('/'),
    routes
})

export default router