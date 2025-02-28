<script setup>
import NavBar from './components/NavBar.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <!-- A full-page light wrapper -->
  <div class="bg-white text-gray-800 min-h-screen">
    <!-- Simple header with NavBar -->
    <header class="leading-relaxed max-h-screen">
      <NavBar />
    </header>
    
    <!-- Main content from Vue Router -->
    <main class="px-4 py-8">
      <RouterView />
    </main>
  </div>
</template>

<style>
/* Minimal global overrides if needed */
</style>
