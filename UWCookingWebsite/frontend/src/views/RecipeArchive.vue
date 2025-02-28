<template>
    <section class="p-6">
      <h1 class="text-3xl font-bold text-blue-600">Recipe Archive</h1>
  
      <!-- Filter Area -->
      <div class="my-4 flex space-x-4">
        <select v-model="filters.difficulty" class="border p-2 rounded">
          <option value="">All Difficulties</option>
          <option value="easy">Easy</option>
          <option value="medium">Medium</option>
          <option value="hard">Hard</option>
        </select>
        <!-- Add more filters as needed -->
      </div>
  
      <!-- Recipe List -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div 
          v-for="recipe in filteredRecipes" 
          :key="recipe.id" 
          class="bg-white shadow p-4 rounded"
          @click="goToRecipeDetail(recipe.id)"
        >
          <img 
            v-if="recipe.image_url" 
            v-lazy="recipe.image_url" 
            class="w-full h-48 object-cover rounded" 
            :alt="recipe.name"
          />
          <h2 class="text-lg font-semibold mt-2">{{ recipe.name }}</h2>
          <p class="text-gray-600 text-sm">Difficulty: {{ recipe.difficulty }}</p>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  
  // Data
  const recipes = ref([])
  const filters = ref({
    difficulty: '',
    // Add more filters as needed
  })
  
  // Fetch recipes on mount
  onMounted(async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/recipes/')
      recipes.value = res.data.recipes
    } catch (error) {
      console.error('Error fetching recipes:', error)
    }
  })
  
  // Computed to apply filters
  const filteredRecipes = computed(() => {
    return recipes.value.filter((recipe) => {
      if (filters.value.difficulty && recipe.difficulty !== filters.value.difficulty) {
        return false
      }
      // Add other filters
      return true
    })
  })
  
  // Navigate to detail
  function goToRecipeDetail(id) {
    router.push(`/recipes/${id}`)
  }
  </script>
  