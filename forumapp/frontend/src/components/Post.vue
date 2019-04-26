<template>
    <v-container fluid>
      <v-container>
        <v-img 
        width="60"
        height="60"
        :src="post.user.profil.avatar" 
        alt="obrazek"
       ></v-img>
      {{ post.title }}
      </v-container>
      
      <v-container>
        user: {{ post.user.username}} 5h temu
        created_at: {{ post.created_at }}
      </v-container>
    
      <v-container>
        <v-img max-width="800" :src="post.image" alt="obrazek"></v-img>
      </v-container>
      
      <v-container>
        {{ post.text }}
      </v-container>

      <v-container>
        like | comments
      </v-container>
    

    <Comment v-for="comment in post.comments" :key="comment.id" :comment="comment"/>
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
// .wrapper {
//   width: 650px;
//   background-color: rgb(110, 110, 110);
//   border: 2px;
//   display: flex;
//   flex-direction: column;
//   padding: 30px;
//   justify-content: center;
//   box-shadow: 7px 15px 35px black;

//   * {
//     display: flex;
//     justify-content: center;
//   }

//   .title-wrapper {
//     color: white;
//     background-color: rgb(36, 33, 33);
//     font-size: 30px;
//     padding: 20px;
//   }
//   .details-wrapper {
//     color: white;
//     background-color: rgb(59, 56, 56);
//     font-size: 12px;
//     padding: 10px;
//     img {
//       max-width: 60px;
//       max-height: 60px;
//     }
//   }
//   img{
//     width: 650px;    
//   }
//   .interactions-wrapper {
//     color: white;
//     padding: 20px;
//     text-align: center;
//     background-color: rgb(109, 111, 255);
//   }
// }
</style>