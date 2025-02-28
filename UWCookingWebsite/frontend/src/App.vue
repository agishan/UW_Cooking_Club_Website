<script setup>
import NavBar from './components/NavBar.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <div>
    <header class="leading-relaxed max-h-screen">
      <NavBar />
    </header>
  
    <main>
      <RouterView />
    </main>
  </div>
</template>


