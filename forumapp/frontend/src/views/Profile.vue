<template>
  <v-container grey lighten-2>
    <v-layout>
      <v-flex shrink mr-4>
        <v-avatar size="200px">
          <img :src="userAvatar" alt="avatar">
        </v-avatar>
      </v-flex>
      <v-flex pl-1 amber shrink></v-flex>
      <v-flex ml-1>
        <v-layout pt-3 pl-3 pb-1 display-1 font-weight-light>{{ username }}</v-layout>

        <v-layout pl-3 pb-1>
          <v-flex>
            <v-icon>outlined_flag</v-icon>
            {{ calculateDate(profile[0].user.date_joined) }}
          </v-flex>
        </v-layout>

        <v-layout pl-3 pb-3>
          <v-flex v-if="profile[0].location">
            <v-icon>location_on</v-icon>
            {{ profile[0].location }}
          </v-flex>
        </v-layout>

        <v-layout
          v-if="profile[0].bio"
          pl-3
          pb-1
        >{{ profile[0].bio }} Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit iure dolorum accusamus iusto ut eveniet quidem debitis deleniti sunt et.
        </v-layout>
      </v-flex>
    </v-layout>

    <v-layout mt-5>
      <v-flex>
        <v-tabs centered color="grey darken-4" dark grow icons-and-text>
          <v-tabs-slider color="amber"></v-tabs-slider>

          <v-tab href="#tab-1">
            Moje posty
            <v-icon>perm_media</v-icon>
          </v-tab>

          <v-tab color="red" href="#tab-2">
            Moje komentarze
            <v-icon>forum</v-icon>
          </v-tab>

          <v-tab-item value="tab-1">
            <v-card color="grey lighten-2" flat >
              <v-card-text>
                <Post v-for="post in posts" :key="post.id" :post="post"></Post>
              </v-card-text>
            </v-card>
          </v-tab-item>

          <v-tab-item value="tab-2">
            <v-card flat color="grey lighten-2">
              <v-card-text>
                <Comment v-for="comment in comments" :key="comment.id" :comment="comment" :post="posts.id"/>
              </v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Post from "../components/Post.vue";
import Comment from "../components/Comment.vue";
import { mapState } from "vuex";
import axios from "axios";
const API = "http://127.0.0.1:8000/api/";

export default {
  components: {
    Post,
    Comment
  },
  data() {
    return {
      profile: [],
      posts: [],
      comments: []
    };
  },
  computed: {
    ...mapState([
      "loggingIn",
      "loginError",
      "accessToken",
      "username",
      "userAvatar"
    ])
  },
  mounted() {
    axios.get(`${API}profiles/?user__username=${this.username}`)
      .then(response => {
        this.profile = response.data;
      });
    axios.get(`${API}posts/?user__username=${this.username}`)
    .then(response => {
      this.posts = response.data;
    });
    axios.get(`${API}comments/?user__username=${this.username}`)
    .then(response => {
      this.comments = response.data;
    });
  },
  methods: {
    calculateDate(date) {
      var dateNow = new Date();
      var createdAt = new Date(date);

      var diffSeconds = Math.abs(dateNow - createdAt) / 1000;

      var months = Math.floor(diffSeconds / 2592000);
      var weeks = Math.floor(diffSeconds / 604800);
      var days = Math.floor(diffSeconds / 86400);
      var hours = Math.floor(diffSeconds / 3600);
      var minutes = Math.floor(diffSeconds / 60);
      var seconds = Math.floor(diffSeconds / 1);

      var choose = null;

       if (seconds < 59) return seconds + (seconds == 1 ? " sekundę temu" : " sek temu");
       if (minutes < 59) return minutes + (minutes == 1 ? " minutę temu" : " min temu");
       if (hours < 59) return hours + (hours == 1 ? " godzinę temu" : " godz temu");
       if (days < 7) return days + (days == 1 ? " dzień temu" : " dni temu");
       if (weeks < 4) return weeks + (weeks == 1 ? " tydzień temu" : " tyg temu");
    }
  }
};
</script>

<style lang="scss" scoped>
</style>