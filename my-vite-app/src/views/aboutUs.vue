<template>
  <div class="events-page">
    <body>
      <div class="banner">
        <div class="header">
          <h1>About Us</h1>
        </div>
      </div>
      <div>
        <h1>Who Are We?</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
          sed do eiusmod tempor incididunt ut labore et dolore magna 
          aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
          ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis 
          aute irure dolor in reprehenderit in voluptate velit esse cillum 
          dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
          non proident, sunt in culpa qui officia deserunt mollit anim id est 
          laborum.</p>
        
        <h1>Our Cooking Philosophy</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
          sed do eiusmod tempor incididunt ut labore et dolore magna 
          aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
          ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis 
          aute irure dolor in reprehenderit in voluptate velit esse cillum 
          dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
          non proident, sunt in culpa qui officia deserunt mollit anim id est 
          laborum.</p>

        <h1>Meet The Team</h1>
      </div>
      <div class="past-events">
          <h2>Admin</h2>
          <div class="past-grid">
            <li v-for="club_members in items" :key="club_members.id" >
              <!-- Construct the image URL by extracting the filename -->
              <div class="event" v-if="club_members.team == 'ADMIN'">
                <img class="event-pic" alt="Event Picture" :src="imageUrl(club_members.images)"/>
                <h3>{{ club_members.name }}</h3>
                <p>{{ club_members.role }}</p>
              </div>
            </li>
          </div>

          <h2>Events</h2>
          <div class="past-grid">
            <li v-for="club_members in items" :key="club_members.id" >
              <!-- Construct the image URL by extracting the filename -->
              <div class="event" v-if="club_members.team == 'EVENTS'">
                <img class="event-pic" alt="Event Picture" :src="imageUrl(club_members.images)"/>
                <h3>{{ club_members.name }}</h3>
                <p>{{ club_members.role }}</p>
              </div>
            </li>
          </div>

          <h2>Content</h2>
          <div class="past-grid">
            <li v-for="club_members in items" :key="club_members.id" >
              <!-- Construct the image URL by extracting the filename -->
              <div class="event" v-if="club_members.team == 'CONTENT'">
                <img class="event-pic" alt="Event Picture" :src="imageUrl(club_members.images)"/>
                <h3>{{ club_members.name }}</h3>
                <p>{{ club_members.role }}</p>
              </div>
            </li>
          </div>
      </div>
      <div>
        <h1>Join The Club</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
          sed do eiusmod tempor incididunt ut labore et dolore magna 
          aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
          ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis 
          aute irure dolor in reprehenderit in voluptate velit esse cillum 
          dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
          non proident, sunt in culpa qui officia deserunt mollit anim id est 
          laborum.</p>
        
        <h1>Have Questions?</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
          sed do eiusmod tempor incididunt ut labore et dolore magna 
          aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
          ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis 
          aute irure dolor in reprehenderit in voluptate velit esse cillum 
          dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
          non proident, sunt in culpa qui officia deserunt mollit anim id est 
          laborum.</p>
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
  name: 'AboutUsPage',
  data() {
    return {
      items: [],
    }
  },
  mounted() {
    fetch('http://127.0.0.1:8000//api/club-members/')
      .then(response => response.json())
      .then(club_memberJSON => {
        // Assuming the API response is something like { recipes: [...] }
        this.items = club_memberJSON.club_members
      })
      .catch(error => {
        console.error('Error fetching club members:', error)
      })
  },
  methods: {
    imageUrl(imagePath) {

      const fileName = imagePath.split('/').pop()
      return `http://127.0.0.1:8000/cdn/media/club_member_images/${fileName}`
    }
  },
}
</script>

<style scoped>
/*.events-page {
  padding: 2rem;
}*/

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

.events-container {
  margin: 40px auto;
  width: 80%;
}

.events-header {
  font-size: 30px;
}
      
.carousel {
  display: flex;
  overflow: hidden;
  justify-content: center;
  align-items: center;
  position: relative;
}
      
.carousel-track {
  display: flex;
  transition: transform 0.5s ease-in-out;
}
      
.event {
  width: 250px;
  background: white;
  margin: 10px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  overflow: hidden;
  text-align: center;
}
      
.event .event-pic {
  width: 100%;
  height: 65%;
  background: gray;
}
      
.event h3 {
  margin: 10px 0;
  color: black;
}
      
.event p {
  font-size: 14px;
  color: gray;
  padding: 0 10px;
}
      
.carousel button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  cursor: pointer;
  padding: 10px;
}
      
.prev { left: 0; }
.next { right: 0; }

.past-events {
  background: #333;
  padding: 40px 0;
  color: white;
}

.past-events h2 {
  font-size: 40px;
}
      
.past-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  width: 80%;
  margin: auto;
  list-style-type: none;
}
      
.footer {
  background: #00897b;
  padding: 20px;
  color: white;
  display: flex;
  justify-content: space-between;
}

.footer .logo {
  width: 1cm;
  height: 1cm;
}
</style>