import { createRouter, createWebHistory } from 'vue-router'

// Import views
import Home from '../views/Home.vue'
import RecipeArchive from '../views/RecipeArchive.vue'
import RecipeDetail from '../views/RecipeDetail.vue'
import Events from '../views/Events.vue'
import About from '../views/About.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/recipes', component: RecipeArchive },
  { path: '/recipes/:id', component: RecipeDetail, props: true },
  { path: '/events', component: Events },
  { path: '/about', component: About }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
