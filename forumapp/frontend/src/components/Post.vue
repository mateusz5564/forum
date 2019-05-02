<template>
    <v-container mb-5 fluid pa-0 style="background-color: #616161">
     <v-card dark >
        <v-layout row align-center>
          <v-flex pa-2 xs-1 md-1 align-self-center>
            <v-img 
              width="60"
              height="60"
              :src="post.user.profil.avatar" 
              alt="obrazek"
            ></v-img>
          </v-flex>
            <v-flex xs-11 md-11 class="display-1">
              {{ post.title }}
            </v-flex>

        </v-layout>
     </v-card>
      
      
      <v-layout align-center justify-start>
        <v-flex pa-2>
          <span class="amber--text font-weight-bold">
            user: {{ post.user.username}} 
          </span>
          created_at: {{ post.created_at }}
        </v-flex>
      </v-layout>
    
      <v-layout>
        <v-flex xs-2>
          <v-img :src="post.image" alt="obrazek"></v-img>
        </v-flex>
      </v-layout>
      
      <v-layout>
        <v-flex>
          {{ post.text }}
        </v-flex>
      </v-layout>

      <v-layout pa-3 justify-space-between grey lighten>
        <v-flex ml-5 headline>
          <v-btn fab dark color="amber">
            <v-icon dark>thumb_up</v-icon>
          </v-btn>
          <span class="font-weight-light white--text body-1" >
          121 lajków
          </span>
        </v-flex>
        <!-- <v-spacer grow></v-spacer> -->
        <v-flex mr-5 headline class="text-xs-right">
          <v-btn fab dark color="amber">
            <v-icon dark>comment</v-icon>
          </v-btn>
          <span class="white--text body-1">
            3 komentarzy
          </span>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex>
          <Comment v-for="comment in post.comments" :key="comment.id" :comment="comment"/>
        </v-flex>
      </v-layout>

    </v-container>
</template>

<script>
import Comment from './Comment.vue';

export default {
  props: ["post"],
  components: {
    Comment
  },
};
</script>

<style lang="scss" scoped>
  .container {
    max-width: 650px;
  }
</style>
