<template>
  <section class="p-6">
    <h1 class="text-3xl font-bold text-blue-600">About Us</h1>
    <p class="mt-2 text-gray-700">We are the UW Cooking Club exec team...</p>

    <div class="mt-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div 
        v-for="member in members" 
        :key="member.id" 
        class="bg-white p-4 shadow rounded"
      >
        <img 
          v-if="member.profile_pic" 
          v-lazy="member.profile_pic" 
          class="w-full h-48 object-cover rounded"
          :alt="member.name"
        />
        <h2 class="text-lg font-semibold mt-2">{{ member.name }}</h2>
        <p class="text-gray-600">{{ member.role }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const members = ref([])

onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/exec-members/')
    members.value = res.data.members
  } catch (error) {
    console.error('Error fetching exec members:', error)
  }
})
</script>
