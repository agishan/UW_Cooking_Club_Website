import { createApp } from 'vue'
import App from './App.vue'
import { createWebHistory, createRouter } from 'vue-router'
import router from './router'
import './main.css'

createApp(App)
  .use(router)
  .mount('#app')
