<template>
  <v-app class="grey lighten-3">
    <Navbar/>
    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import { mapActions } from "vuex";

export default {
  name: "app",
  components: {
    Navbar
  },
  data() {
    return {};
  },
  methods: {
    ...mapActions(["fetchAccessToken", "fetchUserUsername", "fetchUserId", "fetchUserAvatar", "fetchUserRole"])
  },
  created() {
    this.fetchAccessToken();
    this.fetchUserUsername();
    this.fetchUserId();
    this.fetchUserAvatar();
    this.fetchUserRole();
  }
};
</script>

<style lang="scss">
</style>
