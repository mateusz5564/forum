<template>
  <v-layout mb-3 mt-3>
    <v-flex mr-3 shrink>
      <img :src="comment.avatar_url" alt="obrazek" width="40" height="40">
    </v-flex>
    <v-flex>
      <span class="grey--text--lighten-1 subheading font-weight-medium">
        {{ comment.user.username }} {{ comment.created_at }}
        <br>
      </span>

      {{ comment.content }}
      
      <button>like</button>
      {{ comment.number_of_comment_likes }}
      <button>dislike</button>
      {{ comment.number_of_comment_dislikes }}
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: ["comment"]
};
</script>

<style lang="scss" scoped>
</style>
