<template>
    <nav class="w-full bg-blue-600 text-white flex justify-center p-4 space-x-4">
      <router-link to="/" class="hover:underline">Home</router-link>
      <router-link to="/recipes" class="hover:underline">Recipes</router-link>
      <router-link to="/events" class="hover:underline">Events</router-link>
      <router-link to="/about" class="hover:underline">About Us</router-link>
    </nav>
  </template>
  
  <script setup>
  // No special logic needed unless you're toggling mobile menus
  </script>
  
  <style scoped>
  /* If you want minimal scoping, but Tailwind likely covers it */
  </style>
  