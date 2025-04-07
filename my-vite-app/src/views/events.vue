<template>
  <div class="events-page">
    <body>
      <div class="banner">
        <div class="header">
          <h1>Our Events</h1>
        </div>
      </div>
      <div class="events-container">
        <div class="events-header">
          <h2>Upcoming events</h2>
        </div>
          <div class="carousel">
            <button class="prev" onclick="moveSlide(-1)">&#10094;</button>
            <div class="carousel-track">
                <li v-for="event in items" :key="event.id" >
                  <!-- Construct the image URL by extracting the filename -->
                  <router-link :to="`/events/${event.id}`">
                    <div class="event" v-if="new Date(event.date) >= new Date()">
                      <img class="event-pic" alt="Event Picture" :src="imageUrl(event.images)"/>
                      <h3>{{ event.name }}</h3>
                      <p>{{ event.instructor }}</p>
                      <p><strong>{{ event.date }}</strong></p>
                    </div>
                  </router-link>
                </li>
            </div>
            <button class="next" onclick="moveSlide(1)">&#10095;</button>
          </div>
      </div>
      <div class="past-events">
          <h2>Past Events</h2>
          <div class="past-grid">
            <li v-for="event in items" :key="event.id" >
              <!-- Construct the image URL by extracting the filename -->
              <router-link :to="`/events/${event.id}`">
                <div class="event" v-if="new Date(event.date) < new Date()">
                  <img class="event-pic" alt="Event Picture" :src="imageUrl(event.images)"/>
                  <h3>{{ event.name }}</h3>
                  <p>{{ event.instructor }}</p>
                  <p><strong>{{ event.date }}</strong></p>
                </div>
              </router-link>
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
  name: 'EventsPage',
  data() {
    return {
      items: [],
    }
  },
  mounted() {
    fetch('http://127.0.0.1:8000//api/events/')
      .then(response => response.json())
      .then(eventJSON => {
        // Assuming the API response is something like { recipes: [...] }
        this.items = eventJSON.events
      })
      .catch(error => {
        console.error('Error fetching events:', error)
      })
  },
  methods: {
    imageUrl(imagePath) {

      const fileName = imagePath.split('/').pop()
      return `http://127.0.0.1:8000/cdn/media/class_images/${fileName}`
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
  list-style-type: none;
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
