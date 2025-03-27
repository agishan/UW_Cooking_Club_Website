// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue' 
import RecipesPage from '../views/recipes.vue'
import recipe_detail from '../views/recipe_detail.vue'
import EventsPage from '../views/events.vue'
import AboutUsPage from '../views/aboutUs.vue'
import { compile } from 'vue'
import Event_detail from '../views/event_detail.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/recipes', component: RecipesPage },
  { path: '/recipes/:id', component: recipe_detail, props: true },
  { path: '/events', component: EventsPage },
  { path: '/events/:id', component: Event_detail, props: true },
  { path: '/about', component: AboutUsPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
