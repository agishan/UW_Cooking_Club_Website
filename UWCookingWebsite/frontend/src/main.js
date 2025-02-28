// main.js

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// Import Tailwind (and any other global styles) once
import './assets/main.css'

// Create the Vue app instance
const app = createApp(App)

// Use Pinia for state management
app.use(createPinia())

// Use Vue Router
app.use(router)

// Mount the app to #app in index.html
app.mount('#app')
