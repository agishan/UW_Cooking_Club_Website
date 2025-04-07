<template>
    <h1>{{ items.name }}</h1>

     <!-- Below line is in v-if statement cause data fetch from object isn't immediately available,
     important so page doesn't crash  -->
    <img v-if="items.images" :src="imageUrl_Events(items.images)">

    <h1>Date: {{ items.date }}</h1>
    <h1>Taught By: {{ items.instructor }}</h1>
    <h1>Recipes Cooked</h1>
    <div class="recipe-grid" v-if="items.recipes">
      <li v-for="recipe in items.recipes" :key="recipe.id" >
        <!-- Construct the image URL by extracting the filename -->
        <router-link :to="`/recipes/${recipe.id}`">
          <div class="recipe-item">
            <img v-if="recipe.images" class="food-pic" alt="food" :src="imageUrl_Recipes(recipe.images)"/>
            <p v-if="recipe.name">{{ recipe.name }}</p>
          </div>
        </router-link>

      </li>
    </div>

</template>

<script>
export default {
  name: 'Events',
  data() {
    return {
      items: {},
    }
  },
  mounted() {
    fetch(`http://127.0.0.1:8000/api/events/${this.$route.params.id}`)
      .then(response => response.json())
      .then(eventJSON => {
        // Directly assign the event object to "items" variable
        this.items = eventJSON // is expecting only one value (one event), not an array
      })
      .catch(error => {
        console.error('Error fetching event:', error)
      })
  },
  methods: {
    imageUrl_Events(imagePath) {
      const fileName = imagePath.split('/').pop()
      return `http://127.0.0.1:8000/cdn/media/class_images/${fileName}`
    },
    imageUrl_Recipes(imagePath) {
      const fileName = imagePath.split('/').pop()
      return `http://127.0.0.1:8000/cdn/media/recipe_images/${fileName}`
    },
    clickMethod() {
      //add code that you wish to happen on click
    }
  }
}
</script>

<style scoped>
  /* Scoped to this component only */
  body {
      text-align: center;
      margin: 0;
      padding: 0;
      background-color: #ffffff;
  }

  .banner {
      position: relative;
      width: 70%;
      height: 500px;
      margin: 20px auto;
      background: url('../assets/images/banner_temp.png') center/cover no-repeat;
      display: flex;
      align-items: center;
      justify-content: center;
  }

  .header {
      position: absolute;
      background: rgba(255, 255, 255, 0.9); /* White box with slight transparency */
      padding: 100px 200px;
      border-radius: 2px;
  }

  .banner h1 {
      margin: 0;
      font-size: 70px;
      font-weight: bold;
      color: black;
  }

  .container {
      max-width: 900px;
      margin: 20px auto;
      padding: 20px;
  }

  .search-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: gray;
      padding: 10px 15px;
      border-radius: 20px;
      max-width: 1040px;
      margin: 20px auto;
      position: relative;
  }

  .search-bar input {
      flex: 1;
      border: none;
      background: transparent;
      padding: 10px;
      font-size: 16px;
      color: white;
      border-radius: 20px;
  }

  .search-bar input:focus {
      outline: none;
  }

  .search-bar input::placeholder {
      color: white;
      opacity: 0.7;
  }

  .search-icon {
      font-size: 18px;
      color: white;
      cursor: pointer;
  }

  .search-icon {
      margin-right: 10px;
  }

  .menu-icon {
      margin-left: 10px;
  }

  .filter-icon {
      position: absolute;
      right: 40px;
      top: 50%;
      transform: translateY(-50%);
  }

          
  .recipe-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 15px;
      margin-top: 20px;
      list-style-type: none;
  }
          
  .recipe-item {
      background: white;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 20px;
      width: 80%;
      height: 100%;
      margin: auto;
      padding: 15px;
      border-radius: 7px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      margin-bottom: 8px;
  }

  .recipe-item img {
    width: 100%;
    height: 50%;
  }
   
  .footer {
    background: #00897b;
    padding: 20px;
    color: white;
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
  }

  .footer .logo {
    width: 1cm;
    height: 1cm;
  }
  </style>
  