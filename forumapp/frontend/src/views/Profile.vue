<template>
  <v-container grey lighten-2>
    <v-layout>
      <v-flex shrink mr-4>
        <v-avatar size="300px">
          <img :src="userAvatar" alt="avatar">
        </v-avatar>
      </v-flex>
      <v-flex pl-1 amber shrink></v-flex>
      <v-flex ml-1>
        <v-layout pt-3 pl-3 pb-1 display-1 font-weight-light>
          {{ username }}
        </v-layout>

        <v-layout pl-3 pb-1>

          <v-flex>
            <v-icon>outlined_flag</v-icon>
            {{ profile[0].user.date_joined}}
          </v-flex>

        </v-layout>

        <v-layout pl-3 pb-3>
          <v-flex>
            <v-icon>location_on</v-icon>
            {{ profile[0].location }}
          </v-flex>
        </v-layout>

        <v-layout
          pl-3
          pb-1
        >{{ profile[0].bio }} Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit iure dolorum accusamus iusto ut eveniet quidem debitis deleniti sunt et.</v-layout>
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
    axios
      .get(`${API}profiles/?user__username=${this.username}`)
      .then(response => {
        this.profile = response.data;
      });
  }
};
</script>

<style lang="scss" scoped>
</style>