<template>
  <v-container grey lighten-2 accent-2>
    <v-layout>
      <v-flex mr-2 shrink>
        <img :src="comment.avatar_url" alt="obrazek" width="40" height="40">
      </v-flex>

      <v-flex>
        <v-layout justify-space-between row>
          <v-flex shrink>
            <span class="black--text subheading font-weight-medium">{{ comment.user.username }}</span>
            <span class="caption">{{ comment.created_at }}</span>
            <span class="body-1">
              <a class="black--text font-weight-light" @click="expand = !expand">odpowiedz</a>
            </span>
          </v-flex>

          <v-flex shrink>
            <v-btn class="rew-btn" flat icon color="black">
              <v-icon>add_circle</v-icon>
            </v-btn>
            {{ comment.number_of_comment_likes }} : {{ comment.number_of_comment_dislikes }}
            <v-btn class="rew-btn" flat icon color="black">
              <v-icon>remove_circle</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>

        <v-layout>
          <v-flex>{{ comment.content }}</v-flex>
        </v-layout>

        <!-- ODPOWIEDZ -->
        <div>
          <v-layout mt-2>
            <v-flex mr-2 mt-1 shrink>
              <v-expand-transition>
                <div v-show="expand">
                  <img :src="userAvatar" alt="obrazek" width="40" height="40">
                </div>
              </v-expand-transition>
            </v-flex>
            <v-flex>
              <v-expand-transition>
                <div v-show="expand">
                  <v-textarea class="grey lighten-1"></v-textarea>
                </div>
              </v-expand-transition>
            </v-flex>
          </v-layout>

          <v-layout justify-end>
            <v-flex shrink>
              <v-expand-transition>
                <div v-show="expand">
                  <v-btn color="amber" class="send-btn">Wyślij</v-btn>
                </div>
              </v-expand-transition>
            </v-flex>
          </v-layout>
        </div>

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
import { mapState } from "vuex";

export default {
  data: () => ({
    expand: false
  }),
  props: ["comment"],
  components: {
    ChildrenComment
  },
  computed: {
    ...mapState(["username", "userAvatar"])
  }
};
</script>

<style lang="scss" scoped>
.child_comment_pg {
  width: 2px;
}
a:hover {
  color: rgb(255, 194, 11) !important;
}
.send-btn {
  width: 10;
  margin-right: 0;
}
.rew-btn {
  margin: 0;
}
</style>
