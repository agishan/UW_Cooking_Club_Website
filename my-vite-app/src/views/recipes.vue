<template>
  <div class="events-page">
    <body>
      <div class="banner">
        <div class="header">
          <h1>Recipe Archive</h1>
        </div>
      </div>
      <div class="content">
        <div class="search-bar">🔍 
          <i class="search-icon"></i>
          <input type="text" placeholder="Search recipes...">
        </div>
        <div class="recipe-grid">
          <li v-for="recipe in items" :key="recipe.id" >
            <!-- Construct the image URL by extracting the filename -->
            <div class="recipe-item">
              <img class="food-pic" alt="food" :src="imageUrl(recipe.images)"/>
              <p>{{ recipe.name }}</p>
            </div>
        </li>
        </div>
      </div>
        <div class="footer">
            <div>©UWCC 2025</div>
            <div>Our Socials
              <a href="https://www.instagram.com/uwcookingclub/" target="_blank">
                <img class="logo" alt="Instagram Icon" src="../assets/images/insta_icon.png"/>
              </a>
              <a href="https://discord.gg/ZdU7vEFJvn" target="_blank">
                <img class="logo" alt="Discord Icon" src="../assets/images/discord_icon.png"/>
              </a>
            </div>
        </div>
      </body>
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
  