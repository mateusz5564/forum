<template>
<v-form v-model="valid" action="#" @submit.prevent="login" >
      <v-container>
        <v-layout align-content-center>
          <v-flex
            xs12
          >
            <v-text-field
              v-model="firstname"
              :rules="nameRules"
              counter
              label="Login"
              required
            ></v-text-field>
          </v-flex>

        </v-layout>
  

        <v-layout>
            <v-flex
            xs12
            >

                <v-text-field
                :append-icon="show1 ? 'visibility' : 'visibility_off'"
                :rules="nameRules"
                :type="show1 ? 'text' : 'password'"
                name="input-10-1"
                label="Hasło"
                counter
                @click:append="show1 = !show1"
            ></v-text-field>
            </v-flex>
        </v-layout>

        <v-layout align-content-center>
              <v-flex justify-center
              xs12 
              >
                  <v-btn color="amber" @click="submit">Zaloguj się</v-btn>
              </v-flex>
        </v-layout>
  
      </v-container>
    </v-form>
</template>

<script>
    export default {
        name: 'login',
        data () {
            return {
                username: '',
                password: '',
                show1: false,
                rules: {
                    required: value => !!value || 'Required.',
                    min: v => v.length >= 8 || 'Min 8 characters',
                    emailMatch: () => ('The email and password you entered don\'t match')
                } 
            }
        },
        methods: {
            login(){
                
            }
        }
    }

</script>

<style lang="scss" scoped>

</style>