<template>
  <v-container grey lighten-2 accent-2>
    <v-layout>
      <v-flex mr-2 shrink>
        <img :src="commentData[0].avatar_url" alt="obrazek" width="40" height="40">
      </v-flex>

      <v-flex>
        <v-layout justify-space-between row>
          <v-flex shrink>
            <span class="black--text subheading font-weight-medium">{{ commentData[0].user.username }}</span>
            <span class="caption ml-1"> {{ calculateDate(commentData[0].created_at) }}</span>
            <span class="body-1">
              <a v-if="accessToken" class="amber--text text--darken-3 font-weight-light" @click="expand = !expand" > odpowiedz</a>
            </span>
          </v-flex>

          <v-flex shrink>
            <v-btn class="rew-btn" flat icon color="black" @click="likeIt()">
              <v-icon>add_circle</v-icon>
            </v-btn>
            <span class="subheading font-weight-medium ">
              {{ mark(commentData[0].number_of_comment_likes, commentData[0].number_of_comment_dislikes) }}
            </span>
            <v-btn class="rew-btn" flat icon color="black" @click="dislikeIt()">
              <v-icon>remove_circle</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>

      <v-layout wrap>
        <v-flex red>
        
        </v-flex>
      </v-layout>
          {{ commentData[0].content}}


        <!-- ODPOWIEDZ -->
        <div ref="buttn">
          <v-layout mt-2 >
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
                  <v-textarea v-model="commentContent" class="grey lighten-1"></v-textarea>
                </div>
              </v-expand-transition>
            </v-flex>
          </v-layout>

          <v-layout justify-end>
            <v-flex shrink>
              <v-expand-transition>
                <div v-show="expand">
                  <v-btn color="amber" class="send-btn" @click="postComment()" type="submit">Wyślij</v-btn>
                </div>
              </v-expand-transition>
            </v-flex>
          </v-layout>
        </div>

        <v-layout mt-4 v-if="commentData[0].children_comments.length !== 0">
          <v-flex class="child_comment_pg" grey darken-2 mr-3 shrink></v-flex>
          <v-flex>
            <ChildrenComment
              v-for="children in commentData[0].children_comments"
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
import axios from 'axios';
import { bus } from "../main";
const API = "http://127.0.0.1:8000/api/";


export default {
  data () {
   return {
    expand: false,
    commentContent: null,
    commentData: []
   }
 },
  props: ["comment", "post"],
  components: {
    ChildrenComment
  },
  methods: {
    mark: function(likes, dislikes) {
      return (likes - dislikes)
    },
    postComment() {
      axios.post('http://127.0.0.1:8000/api/comment/create/', {
        content: this.commentContent,
        user: this.userId,
        post: this.post,
        parent_id: this.comment.id
      }).then((response) => {
        this.expand = false;
        this.commentContent = null;
        this.fetchData();
      })
      .catch((e) => {
        console.error(e)
      })
    },
    fetchData() {
      axios
     .get(`${API}comments/?id=${this.comment.id}`)
     .then(response => {
       this.commentData = response.data;
     })
    },
    likeIt() {
      axios
        .get(`${API}comments_rating/create/?user=${this.userId}&comment=${this.comment.id}`)
        .then(response => {
          if (response.data.length == 0) {
            axios
              .post(`${API}comments_rating/create/`, {
                is_positive: true,
                user: this.userId,
                comment: this.comment.id,
              })
              .then(response => {
                this.commentData = response.data;
                this.fetchData();
              });
          } else {
            console.log(this.comment.id)
            console.log("już głosowałeś");
            console.log(response.data);
          }
        })
        .catch(e => {});
    }, 
    dislikeIt() {
      axios
        .get(`${API}comments_rating/create/?user=${this.userId}&comment=${this.comment.id}`)
        .then(response => {
          if (response.data.length == 0) {
            axios
              .post(`${API}comments_rating/create/`, {
                is_positive: false,
                user: this.userId,
                comment: this.comment.id
              })
              .then(response => {
                this.commentData = response.data;
                this.fetchData();
              });
          } else {
            console.log(this.comment.id)
            console.log("już głosowałeś");
            console.log(response.data);
          }
        })
        .catch(e => {});
    },       
    calculateDate(date) {
      var dateNow = new Date();
      var createdAt = new Date(date);

      var diffSeconds = Math.abs(dateNow - createdAt) / 1000;

      var months = Math.floor(diffSeconds / 2592000);
      var weeks = Math.floor(diffSeconds / 604800);
      var days = Math.floor(diffSeconds / 86400);
      var hours = Math.floor(diffSeconds / 3600);
      var minutes = Math.floor(diffSeconds / 60);
      var seconds = Math.floor(diffSeconds / 1);

      var choose = null;

       if (seconds < 59) return seconds + (seconds == 1 ? " sekundę temu" : " sek temu");
       if (minutes < 59) return minutes + (minutes == 1 ? " minutę temu" : " min temu");
       if (hours < 24) return hours + (hours == 1 ? " godzinę temu" : " godz temu");
       if (days < 7) return days + (days == 1 ? " dzień temu" : " dni temu");
       if (weeks < 4) return weeks + (weeks == 1 ? " tydzień temu" : " tyg temu");
    }
  },
  mounted() {
    // this.fetchData();
    bus.$on("updateComment", () => {
      this.fetchData();
    })
  },
  created() {
    this.fetchData();
  },
  computed: {
    ...mapState(["username", "userAvatar", "userId", "accessToken"])
  },

};
</script>

<style lang="scss" scoped>
.container {
  max-width: 650px;
}
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
