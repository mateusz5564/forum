<template>
  <v-app class="grey lighten-3">
    <Navbar />
    <v-content>
      
      <v-container fluid>
        <router-view></router-view>
      </v-container>

    </v-content>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
 name: 'app',
 components: {
   Navbar
 },
 data () {
   return {
     
   }
 },
}
</script>

<style lang="scss">

</style>