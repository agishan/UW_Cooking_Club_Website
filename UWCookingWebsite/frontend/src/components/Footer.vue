<template>
    <footer class="bg-gray-800 text-white p-4 mt-8">
      <div class="container mx-auto">
        <p>© UW Cooking Club</p>
        <div class="flex space-x-4 mt-2">
          <a :href="contactData.discord" target="_blank" class="underline">
            Discord
          </a>
          <a :href="contactData.instagram" target="_blank" class="underline">
            Instagram
          </a>
        </div>
        <p v-if="contactData.email" class="mt-2">
          Contact: {{ contactData.email }}
        </p>
      </div>
    </footer>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios' // or import apiClient if used
  
  const contactData = ref({})
  
  // Fetch contact info on mount
  onMounted(async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/contact/')
      contactData.value = res.data
    } catch (error) {
      console.error('Error fetching contact info', error)
    }
  })
  </script>
  