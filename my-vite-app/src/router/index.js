// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue' // or wherever you placed it
import RecipesPage from '../views/recipes.vue'
import EventsPage from '../views/events.vue'
import AboutUsPage from '../views/aboutUs.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/recipes', component: RecipesPage },
  { path: '/events', component: EventsPage },
  { path: '/about', component: AboutUsPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
