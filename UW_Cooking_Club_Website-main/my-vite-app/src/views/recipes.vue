<template>
    <div>
      <h1>Recipes</h1>
      <ul>
        <!-- Loop through each recipe item -->
        <li v-for="recipe in items" :key="recipe.id">
          <h2>{{ recipe.name }}</h2>
  
          <!-- Construct the image URL by extracting the filename -->
          <img
            :src="imageUrl(recipe.images)"
            alt="Recipe Image"
          />
  
          <p>Description: {{ recipe.description }}</p>
          <p>Difficulty Level: {{ recipe.difficulty }}</p>
          <p>Prep Time: {{ recipe.prep_time }}</p>
          <p>Cook Time: {{ recipe.cook_time }}</p>
          <p>Total Time: {{ recipe.total_time }}</p>
          <p>Serving Size: {{ recipe.serving_size }}</p>
          <p>Equipment: {{ recipe.equipment }}</p>
          <p>Ingredients: {{ recipe.ingredients }}</p>
          <p>Procedure: {{ recipe.procedure }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Recipes',
    data() {
      return {
        items: [],
      }
    },
    mounted() {
      fetch('http://127.0.0.1:8000//api/recipes/')
        .then(response => response.json())
        .then(recipeJSON => {
          // Assuming the API response is something like { recipes: [...] }
          this.items = recipeJSON.recipes
        })
        .catch(error => {
          console.error('Error fetching recipes:', error)
        })
    },
    methods: {
      imageUrl(imagePath) {

        const fileName = imagePath.split('/').pop()
        return `http://127.0.0.1:8000/cdn/media/recipe_images/${fileName}`
      }
    }
  }
  </script>
  
  <style scoped>
  /* Scoped to this component only */
  h1 {
    margin-bottom: 1rem;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    margin-bottom: 2rem;
  }
  img {
    height: 100px;
    display: block;
    margin: 0.5rem 0;
  }
  </style>
  