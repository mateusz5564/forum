<template>
  <v-layout mb-3 mt-3>
    <v-flex mr-3 shrink>
      <img :src="comment.avatar_url" alt="obrazek" width="40" height="40">
    </v-flex>

    <v-flex>
      <v-layout justify-space-between row>
        <v-flex shrink>
          <span class="black--text subheading font-weight-medium">{{ comment.user.username }}</span>
          <span class="caption">{{ comment.created_at }}</span>
        </v-flex>

        <v-flex shrink>
          <v-btn class="rew-btn" flat icon color="black">
            <v-icon>add_circle</v-icon>
          </v-btn>
          {{ comment.number_of_comment_likes }}0 : 0{{ comment.number_of_comment_dislikes }}
          <v-btn class="rew-btn" flat icon color="black">
            <v-icon>remove_circle</v-icon>
          </v-btn>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex>{{ comment.content }}</v-flex>
      </v-layout>

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
.rew-btn {
  margin: 0;
}
</style>
