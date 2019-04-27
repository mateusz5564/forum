<template>
    <nav>
            
        <v-toolbar dark app>
            <v-toolbar-title class="amber--text">
                DISCUSSR
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-btn class="amber--text">Nowe</v-btn>
                <v-btn class="amber--text">Oczekujące</v-btn>
                <v-btn class="amber--text">Top</v-btn>
                <v-btn class="amber--text">Losowe</v-btn>
                <v-btn color="amber" class="black--text">Rejestracja</v-btn>
            </v-toolbar-items>
        </v-toolbar>

    <v-navigation-drawer
      v-model="drawer"
      :mini-variant.sync="mini"
      app
      dark
    >
      <v-toolbar flat class="transparent">
        <v-list class="pa-0">
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <img src="https://randomuser.me/api/portraits/men/85.jpg">
            </v-list-tile-avatar>
  
            <v-list-tile-content>
              <v-list-tile-title>Username</v-list-tile-title>
            </v-list-tile-content>
  
            <v-list-tile-action>
              <v-btn
                icon
                @click.stop="mini = !mini"
              >
                <v-icon @click.stop="mini = !mini">chevron_left</v-icon>
              </v-btn>
            </v-list-tile-action>
          </v-list-tile>
        </v-list>
      </v-toolbar>
  
      <v-list class="pt-0" dense>
        <v-divider></v-divider>
  
        <v-list-tile
          v-for="item in items"
          :key="item.title"
          @click=""
        >
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
  
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
</nav>
</template>

<script>
    export default {
        data(){
            return{
                drawer: true,
                items: [
                    { title: 'Ulubione', icon: 'dashboard' },
                    { title: 'Moje posty', icon: 'question_answer' }
                ],
                mini: true,
                right: null
                }
            }
        }
</script>

<style lang="scss" scoped>

</style>