<template>
  <v-container amber accent-2>
    <v-layout>
      <v-flex mr-2 shrink>
        <img :src="comment.avatar_url" alt="obrazek" width="40" height="40">
      </v-flex>

      <v-flex>
        <v-layout justify-space-between row>
          <v-flex shrink>
            <span class="black--text subheading font-weight-medium">
              {{ comment.user.username }} {{ comment.created_at }}
              <br>
            </span>
          </v-flex>

          <v-flex xs3>
            <v-btn flat icon color="black">
              <v-icon>add_circle</v-icon>
            </v-btn>
            {{ comment.number_of_comment_likes }} : {{ comment.number_of_comment_dislikes }}
            <v-btn flat icon color="black">
              <v-icon>remove_circle</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>

        {{ comment.content }}
        <v-layout mt-4 v-if="comment.children_comments.length !== 0">
          <v-flex class="child_comment_pg" grey darken-2 mr-3 shrink></v-flex>
          <v-flex>
            <ChildrenComment
              v-for="children in comment.children_comments"
              :key="children.id"
              :comment="children"
            />
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ChildrenComment from "./ChildrenComment.vue";

export default {
  props: ["comment"],
  components: {
    ChildrenComment
  }
};
</script>

<style lang="scss" scoped>
.child_comment_pg {
  width: 2px;
}
</style>
