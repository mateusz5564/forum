<template>
  <v-container>
    <v-form @submit.prevent="register">
      <v-layout>
        <v-flex mt-3 mb-3 justify-center md4 offset-md4>
          <v-alert :value="true" type="success" outline>
            <span>Pomyślnie zarejestrowano!</span>
          </v-alert>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex mt-3 mb-3 justify-center md4 offset-md4>
          <v-alert :value="true" type="error" outline>
            <span>Nie udało się zarejestrować!</span>
          </v-alert>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex md4 offset-md4>
          <v-text-field v-model="username" counter label="Login"></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex md4 offset-md4>
          <v-text-field v-model="email" counter label="Email"></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex md4 offset-md4>
          <v-text-field
            v-model="password"
            :append-icon="showPassword ? 'visibility' : 'visibility_off'"
            :type="showPassword ? 'text' : 'password'"
            counter
            label="Hasło"
            @click:append="showPassword = !showPassword"
          ></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex md4 offset-md4>
          <v-text-field
            v-model="repeatPassword"
            :append-icon="showRepeatPassword ? 'visibility' : 'visibility_off'"
            :type="showRepeatPassword ? 'text' : 'password'"
            counter
            label="Powtórz hasło"
            @click:append="showRepeatPassword = !showRepeatPassword"
          ></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex md4 offset-md4>
          <v-btn color="amber" type="submit">Zarejestruj się</v-btn>
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
      email: "",
      password: "",
      repeatPassword: "",

      showPassword: false,
      showRepeatPassword: false,

      rules: {
          
      }
    };
  },
  computed: {
      ...mapState(["loggingIn", "loginError", "accessToken"])
  },
  methods: {
      ...mapActions(["doRegister"]),
      register() {
          this.doRegister({
              username: this.username,
              email: this.email,
              password: this.password
          });
      }
  }
};
</script>

<style lang="scss" scoped>
</style>