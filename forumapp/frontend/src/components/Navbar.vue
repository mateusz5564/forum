<template>
  <nav>
    <!-- top menu -->
    <v-toolbar dark app>
      <v-toolbar-title class="amber--text">DISCUSSR</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn to="/posts" class="amber--text">Nowe</v-btn>
        <v-btn to="/waiting" class="amber--text">Oczekujące</v-btn>
        <v-btn v-if="!accessToken" color="amber" to="/login" class="black--text">Logowanie</v-btn>
        <v-btn v-if="!accessToken" to="/register" class="amber--text">
          <v-icon left>how_to_reg</v-icon>Rejestracja
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <!-- left menu -->
    <v-navigation-drawer v-model="drawer" :mini-variant.sync="mini" app dark>
      <v-toolbar flat class="transparent">
        <v-list class="pa-0">
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <img v-if="username" :src="userAvatar">
              <v-icon v-if="!username">account_box</v-icon>
            </v-list-tile-avatar>

            <v-list-tile-content>
              <span v-if="!username">
                <v-btn to="/login" outline color="amber">Zaloguj się</v-btn>
              </span>
              <v-list-tile-title>{{ username }}</v-list-tile-title>
            </v-list-tile-content>

            <v-list-tile-action>
              <v-btn icon @click.stop="mini = !mini">
                <v-icon @click.stop="mini = !mini">chevron_left</v-icon>
              </v-btn>
            </v-list-tile-action>
          </v-list-tile>
        </v-list>
      </v-toolbar>

      <v-list class="pt-0" dense>
        <v-divider></v-divider>

        <template v-slot:activator>
          <v-list-tile>
            <v-list-tile-title>Users</v-list-tile-title>
          </v-list-tile>
        </template>

        <!-- profil -->
        <v-list-tile v-if="accessToken" to="/profile" @click>
          <v-list-tile-action>
            <v-icon>account_circle</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>Profil</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <!-- dodaj post-->
        <v-list-tile v-if="accessToken" to="/newPost" @click>
          <v-list-tile-action>
            <v-icon>add_to_photos</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>Dodaj post</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <!-- moje posty -->
        <!-- <v-list-tile v-if="accessToken" @click>
          <v-list-tile-action>
            <v-icon>question_answer</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>Moje posty</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile> -->

        <v-divider></v-divider>

        <!-- wylogowywanie -->
        <v-list-tile v-if="accessToken" @click>
          <v-list-tile-action>
            <v-icon >exit_to_app</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title @click="logout">Wyloguj się</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
import { mapActions } from "vuex";
import { mapState } from "vuex";

export default {
  data() {
    return {
      drawer: true,
      items: [
        { title: "Profil", icon: "account_circle" },
        { title: "Ulubione", icon: "star" },
        { title: "Moje posty", icon: "question_answer" }
      ],
      mini: true,
      right: null
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
  methods: {
    ...mapActions(["logout"])
  }
};
</script>

<style lang="scss" scoped>
</style>
