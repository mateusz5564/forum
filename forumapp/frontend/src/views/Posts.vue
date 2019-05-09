<template>
    <v-content>
      <router-view></router-view>
        <Post v-for="post in posts" :key="post.id" :post="post"> </Post>
    </v-content>
</template>

<script>
import Post from '../components/Post.vue';
import axios from 'axios';
const API = "http://127.0.0.1:8000/api/";

export default {
 name: 'app',
 components: {
   Post
 },
 data () {
   return {
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

</style>
