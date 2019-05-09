<template>
  <v-container grey lighten-2>
    <v-layout>
      <v-flex shrink>
        <v-avatar size="300px">
          <img :src="userAvatar" alt="avatar">
        </v-avatar>
      </v-flex>
      <v-flex ml-4 grey lighten-1>
        {{ username }}
        <br>location
        <br>bio
        <br>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";
const API = "http://127.0.0.1:8000/api/";

export default {
  data() {
    return {
      profile: []
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
    axios.get(`${API}profiles/`).then(response => {
      this.profile = response.data;
    });
  }
};
</script>

<style lang="scss" scoped>
</style>