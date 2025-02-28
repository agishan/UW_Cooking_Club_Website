<template>
    <section class="p-6">
      <h1 class="text-3xl font-bold text-blue-600">Welcome to UW Cooking Club</h1>
      <p class="text-lg mt-2 text-gray-700">
        Who We Are: We are a club dedicated to ...
      </p>
  
      <!-- Latest Event -->
      <div class="mt-8 bg-white p-4 shadow rounded">
        <h2 class="text-xl font-semibold text-blue-500">Latest Event</h2>
        <div v-if="latestEvent">
          <img 
            v-lazy="latestEvent.image_url" 
            alt="Latest Event" 
            class="mt-2 w-full max-h-64 object-cover rounded"
          />
          <p class="mt-2 text-gray-600">{{ latestEvent.description }}</p>
        </div>
        <p v-else>Loading latest event...</p>
      </div>
  
      <!-- Links to Social Media -->
      <div class="mt-4">
        <a href="https://instagram.com/uwcookingclub" class="text-blue-600 hover:underline" target="_blank">
          Instagram
        </a>
        |
        <a href="https://discord.gg/12345" class="text-blue-600 hover:underline" target="_blank">
          Discord
        </a>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios' // or import apiClient if used
  const latestEvent = ref(null)
  
  onMounted(async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/events/latest/')
      latestEvent.value = response.data
    } catch (error) {
      console.error('Error fetching latest event:', error)
    }
  })
  </script>
  
  <style scoped>
  </style>
  