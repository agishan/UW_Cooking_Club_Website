<template>
<h1>Recipe</h1>
<u1 v-for="recipe in items" :key="recipe.id">
    <li>
        {{recipe.name}}
        <div></div>
        <img :src="'http://127.0.0.1:8000/media/recipe_images/'.concat(recipe.images.split('/')[recipe.images.split('/').length-1])">
        <div></div>
        Description: {{recipe.description}}
        <div></div>
        Difficulty Level: {{recipe.difficulty}}
        <div></div>
        Prep Time: {{recipe.prep_time}}
        <div></div>
        Cook Time: {{recipe.cook_time}}
        <div></div>
        Total Time: {{recipe.total_time}}
        <div></div>
        Serving Size: {{recipe.serving_size}}
        <div></div>
        Equipment: {{recipe.equipment}}
        <div></div>
        Ingredients: {{recipe.ingredients}}
        <div></div>
        Procedure: {{recipe.procedure}}
        <div></div>
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
img {
  height: 100px ;
}
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
