<template>
    <header class="header">
      <img
        class="logo"
        alt="UW Cooking Club Logo"
        src="../assets/uwcooking_icon.png"
      />
      <nav class="nav">
        <router-link to="/">Home</router-link>
        <router-link to="/recipes">Recipes</router-link>
        <router-link to="/events">Events</router-link>
        <router-link to="/about">About Us</router-link>
      </nav>
    </header>
  </template>
  
  <script>
  export default {
    name: 'NavBar',
  }
  </script>
  
  <style scoped>
  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #ffffff;
    padding: 1rem 2rem;
    border-bottom: 1px solid #ddd;
  }
  
  .logo {
    height: 60px;
  }
  
  .nav {
    display: flex;
  }

  .nav a {
    margin: 0 1rem;
    text-decoration: none;
    color: #333;
    font-weight: 500;
  }
  
  .nav a:hover {
    color: #666;
  }
  </style>
  