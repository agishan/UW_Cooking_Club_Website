<template>
    <section class="p-6">
      <div v-if="recipe">
        <h1 class="text-3xl font-bold text-blue-600">{{ recipe.name }}</h1>
        <img 
          v-if="recipe.image_url" 
          v-lazy="recipe.image_url" 
          class="w-full max-h-64 object-cover mt-4 rounded"
          :alt="recipe.name"
        />
        <p class="mt-4 text-gray-700">{{ recipe.description }}</p>
        
        <div class="mt-4">
          <p><strong>Ingredients:</strong> {{ recipe.ingredients }}</p>
          <p><strong>Steps:</strong> {{ recipe.steps }}</p>
          <p><strong>Cook Time:</strong> {{ recipe.cook_time }}</p>
          <p><strong>Difficulty:</strong> {{ recipe.difficulty }}</p>
        </div>
  
        <button 
          @click="generateShoppingList" 
          class="mt-4 bg-blue-600 text-white px-4 py-2 rounded"
        >
          Generate Shopping List
        </button>
      </div>
      <p v-else>Loading recipe...</p>
    </section>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useRoute } from 'vue-router'
  
  const route = useRoute()
  const recipeId = route.params.id
  
  const recipe = ref(null)
  
  onMounted(async () => {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/api/recipes/${recipeId}/`)
      recipe.value = res.data
    } catch (error) {
      console.error('Error fetching recipe details:', error)
    }
  })
  
  // Example function
  function generateShoppingList() {
    alert(`Shopping list for: ${recipe.value.name}`)
    // Alternatively, navigate to another route or open a modal
  }
  </script>
  