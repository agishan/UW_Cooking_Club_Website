import { createApp } from 'vue'
import App from './App.vue'
import { createWebHistory, createRouter } from 'vue-router'

import recipes from './components/recipes.vue'
import testing from './components/testing.vue'

const routes = [
  { path: '/', component: testing },
  { path: '/recipes', component: recipes },
]

const router = createRouter({
  history: createWebHistory(),  // Use createWebHistory here
  routes,
})

createApp(App)
    .use(router)
    .mount('#app')