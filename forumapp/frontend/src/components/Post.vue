<template>
  <div class="wrapper">
    <div class="title-wrapper">{{ post.title }}</div>
    <div class="details-wrapper">user: {{ post.user.username}} <br/> created_at: {{ post.created_at }}</div>
    <div class="img-wrapper">
      <img :src="post.image" alt="obrazek">
    </div>
    <div class="text-wrapper">{{ post.text }}</div>
    <div class="interactions-wrapper">like | comments</div>
    <Comment v-for="comment in post.comments" :key="comment.id" :comment="comment"/>
  </div>
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
.wrapper {
  width: 650px;
  background-color: rgb(110, 110, 110);
  border: 2px;
  display: flex;
  flex-direction: column;
  padding: 30px;
  justify-content: center;
  box-shadow: 7px 15px 35px black;

  * {
    display: flex;
    justify-content: center;
  }

  .title-wrapper {
    color: white;
    background-color: rgb(36, 33, 33);
    font-size: 30px;
    padding: 20px;
  }
  .details-wrapper {
    color: white;
    background-color: rgb(59, 56, 56);
    font-size: 12px;
    padding: 10px;
  }
  img{
    width: 650px;    
  }
  .interactions-wrapper {
    color: white;
    padding: 20px;
    text-align: center;
    background-color: rgb(109, 111, 255);
  }
}
</style>