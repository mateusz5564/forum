<template>
  <v-container>
    <v-form @submit.prevent="login">
      <v-layout align-content-center>
        <v-flex v-if="accessToken" mt-3 mb-3 justify-center md5 offset-md3>
          <v-alert :value="true" type="success" outline>
            <span>Jesteś zalogowany!</span>
          </v-alert>
        </v-flex>
      </v-layout>

      <v-layout align-content-center>
        <v-flex mt-3 mb-3 justify-center md5 offset-md3>
          <v-alert v-if="loginError" :value="true" type="error" outline>
            <span>{{ loginError }}</span>
          </v-alert>
        </v-flex>
      </v-layout>

      <v-layout align-content-center>
        <v-flex md5 offset-md3>
          <v-text-field v-model="username" counter label="Login" required></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex md5 offset-md3>
          <v-text-field
            v-model="password"
            :append-icon="show1 ? 'visibility' : 'visibility_off'"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Hasło"
            counter
            @click:append="show1 = !show1"
          ></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout align-content-center>
        <v-flex justify-center md3 offset-md5>
          <v-btn color="amber" type="submit">Zaloguj się</v-btn>
        </v-flex>
      </v-layout>
    </v-form>
  </v-container>
</template>

<script>
import axios from "axios";
import { mapState, mapActions } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",

      show1: false
    };
  },
  computed: {
    ...mapState(["loggingIn", "loginError", "accessToken"])
  },
  methods: {
    ...mapActions(["doLogin"]),
    login() {
      this.doLogin({
        username: this.username,
        password: this.password
      });
    }
  }
};
</script>

<style lang="scss" scoped>
</style>