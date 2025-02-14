<template>
<h1>Recipe</h1>
<u1 v-for="recipe in items" :key="recipe.id">
    <li>
        <div></div>
        <!-- <img src="{{recipe.images.url}}"> -->
         AMOGUS
        <div></div>
       
    </li>
</u1>



</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
data() {
  return {
    items: []
  }
},
mounted () {
    fetch('http://127.0.0.1:8000/recipeAPI/')
      .then(response => {response.json().then(recipeJSON => (this.items = recipeJSON.recipes))})
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
