<template>
    <section class="p-6">
      <h1 class="text-3xl font-bold text-blue-600">Events</h1>
      <div class="mt-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div 
          v-for="event in events" 
          :key="event.id" 
          class="bg-white shadow rounded p-4"
        >
          <img 
            v-if="event.image_url" 
            v-lazy="event.image_url" 
            class="w-full h-48 object-cover rounded"
            :alt="event.name"
          />
          <h2 class="text-xl font-semibold mt-2">{{ event.name }}</h2>
          <p class="text-gray-600 text-sm">{{ event.date }}</p>
          
          <!-- Link to related recipe if available -->
          <div class="mt-2" v-if="event.recipe_id">
            <router-link 
              :to="`/recipes/${event.recipe_id}`" 
              class="text-blue-500 hover:underline"
            >
              View Related Recipe
            </router-link>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const events = ref([])
  
  onMounted(async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/events/')
      events.value = res.data.events
    } catch (error) {
      console.error('Error fetching events:', error)
    }
  })
  </script>
  