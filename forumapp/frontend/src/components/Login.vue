<template>
  <v-container>
    <v-form @submit.prevent="login">
      <v-layout align-content-center>
        <v-flex v-if="accessToken" mt-3 mb-3 justify-center md4 offset-md4>
          <v-alert :value="true" type="success" outline>
            <span>Jesteś zalogowany!</span>
          </v-alert>
        </v-flex>
      </v-layout>

      <v-layout align-content-center>
        <v-flex mt-3 mb-3 justify-center md4 offset-md4>
          <v-alert v-if="loginError" :value="true" type="error" outline>
            <span>{{ loginError }}</span>
          </v-alert>
        </v-flex>
      </v-layout>

      <v-layout align-content-center>
        <v-flex md4 offset-md4>
          <v-text-field v-model="username" counter label="Login" required></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex md4 offset-md4>
          <v-text-field
            v-model="password"
            :append-icon="show ? 'visibility' : 'visibility_off'"
            :type="show ? 'text' : 'password'"
            label="Hasło"
            counter
            required
            @click:append="show = !show"
          ></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout align-content-center>
        <v-flex justify-center md4 offset-md4>
          <v-btn color="amber" type="submit">Zaloguj się</v-btn>
        </v-flex>
      </v-layout>
    </v-form>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data() {
    return {
      username: "",
      password: "",

      show: false
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