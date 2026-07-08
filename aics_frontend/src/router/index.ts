import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Chatbot from '@/views/Chatbot.vue'
import Logs from '@/views/Logs.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/chatbot',
      name: 'chatbot',
      component: Chatbot
    },
    {
      path: '/logs',
      name: 'logs',
      component: Logs
    }
  ],
})

export default router
