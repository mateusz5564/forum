<template>
<div>
 <Post v-for="post in posts" :key="post.id" :post="post"> </Post>
</div>
</template>

<script>
import Post from './components/Post.vue';
import axios from 'axios';

const API = "http://127.0.0.1:8000/api/";

export default {
 name: 'app',
 components: {
   Post
 },
 data () {
   return {
     msg: "12345",
     posts: []
   }
 },
 mounted () {
   axios
     .get(`${API}posts/`)
     .then(response => {
       this.posts = response.data
     })
 },
}
</script>

<style lang="scss">
  body{
    background-color: rgb(173, 162, 162);
    display: flex;
    justify-content: center;
  }
</style>
