<template>
  <v-container mb-5 pa-0 style="background-color: #616161">
    <v-layout>
      <v-flex>
        <v-card dark>
          <v-layout row align-center>
            <v-flex pa-2 xs-1 md-1 shrink align-self-center>
              <v-img width="60" height="60" :src="postData[0].user.profil.avatar" alt="obrazek"></v-img>
            </v-flex>
            <v-flex xs-11 md-11 class="headline">{{ postData[0].title }}</v-flex>
          </v-layout>
        </v-card>

        <v-layout align-center justify-start>
          <v-flex pa-2>
            <span class="amber--text font-weight-bold subheading">{{ postData[0].user.username}}</span>
            <span
              class="ml-1 grey--text text--lighten-2 caption"
            >{{ calculateDate(postData[0].created_at) }}</span>
          </v-flex>
          <v-flex v-if="isStaff && waiting()" shrink>
            <v-btn flat small depressed outline @click="changeStatus()">akceptuj</v-btn>
          </v-flex>
        </v-layout>

        <v-layout>
          <v-flex v-if='postData[0].text !== "null"' black pa-3 class="display-1 amber--text text--accent-5">
            <div class="formText">

              {{ postData[0].text }}

            </div>
          </v-flex>
        </v-layout>



        <v-layout>
          <v-flex xs-2>
            <v-img :src="postData[0].image" alt="obrazek"></v-img>
          </v-flex>
        </v-layout>


        <v-layout pa-3 justify-space-between grey lighten>
          <v-flex ml-5 headline>
            <v-btn fab dark color="amber" @click="rateComment()">
              <v-icon dark>thumb_up</v-icon>
            </v-btn>
            <span
              class="font-weight-light white--text body-1"
            >{{ postData[0].number_of_post_likes }} lajków</span>
          </v-flex>

          <v-flex mr-5 headline class="text-xs-right">
            <v-btn fab dark color="amber" @click="expandComments = !expandComments">
              <v-icon dark>comment</v-icon>
            </v-btn>
            <span class="white--text body-1">{{ postData[0].number_of_comments }} komentarzy</span>
          </v-flex>
        </v-layout>

        <v-layout>
          <v-flex text-xs-center grey lighten-1 pb-2 pt-2>
            <span class="body-1 ml-2">
              <a
                v-if="accessToken"
                class="white--text font-weight-bold subheading"
                @click="expand = !expand"
              >
                odpowiedz
                <v-icon color="amber lighten-2">arrow_downward</v-icon>
              </a>
            </span>
          </v-flex>
        </v-layout>

        <!-- ODPOWIEDŹ -->

        <v-layout grey v-if="expand" pt-4>
          <v-flex mr-2 mt-1 ml-4 shrink>
            <v-expand-transition>
              <div v-show="expand">
                <img :src="userAvatar" alt="obrazek" width="40" height="40">
              </div>
            </v-expand-transition>
          </v-flex>
          <v-flex mr-4>
            <v-expand-transition>
              <div v-show="expand">
                <v-textarea v-model="commentContent" class="grey lighten-1"></v-textarea>
              </div>
            </v-expand-transition>
          </v-flex>
        </v-layout>

        <v-layout grey class="xd" justify-end>
          <v-flex mr-3 shrink>
            <v-expand-transition>
              <div v-show="expand">
                <v-btn color="amber" class="send-btn" @click="postComment()" type="submit">Wyślij</v-btn>
              </div>
            </v-expand-transition>
          </v-flex>
        </v-layout>


        <v-layout>
          <v-flex v-show="expandComments">
            <v-expand-transition>
              <div v-show="expandComments">
                <Comment
                  v-for="comment in postData[0].comments"
                  :key="comment.id"
                  :comment="comment"
                  :post="postData[0].id"
                />
              </div>
            </v-expand-transition>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Comment from "./Comment.vue";
import { mapState } from "vuex";
import axios from "axios";
import { bus } from "../main";
const API = "http://127.0.0.1:8000/api/";

export default {
  data() {
    return {
      expand: false,
      expandComments: false,
      postData: []
    };
  },
  props: ["post"],
  components: {
    Comment
  },
  methods: {
    mark: function(likes, dislikes) {
      return likes - dislikes;
    },
    waiting: function () {
      return this.$route.path.indexOf('/waiting') === 0
    },
    postComment() {
      axios
        .post("http://127.0.0.1:8000/api/comment/create/", {
          content: this.commentContent,
          user: this.userId,
          post: this.post.id
        })
        .then(response => {
          this.expand = false;
          this.commentContent = null;
          this.expandComments = true;
          this.fetchData();
        })
        .catch(e => {
          console.error(e);
        });
    },
    changeStatus() {
      axios
        .put(`http://127.0.0.1:8000/api/post/update/${this.post.id}/`, {
          is_accepted: true
        })
        .then(response => {
          this.updatePosts();
        })
        .catch(e => {
          console.error(e);
        });
    },
    fetchData() {
      axios.get(`${API}posts/?id=${this.post.id}`).then(response => {
        this.postData = response.data;
      });
    },
    updatePosts: function () {
      bus.$emit('updatePosts');
    },
    rateComment() {
      axios
        .get(
          `${API}post_rating/create/?user=${this.userId}&post=${this.post.id}`
        )
        .then(response => {
          if (response.data.length == 0) {
            axios
              .post(`${API}post_rating/create/`, {
                user: this.userId,
                post: this.post.id
              })
              .then(response => {
                this.postData = response.data;
                this.fetchData();
              });
          } else {
            console.log(this.post.id);
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

      if (seconds < 59)
        return seconds + (seconds == 1 ? " sekundę temu" : " sek temu");
      if (minutes < 59)
        return minutes + (minutes == 1 ? " minutę temu" : " min temu");
      if (hours < 24)
        return hours + (hours == 1 ? " godzinę temu" : " godz temu");
      if (days < 7) return days + (days == 1 ? " dzień temu" : " dni temu");
      if (weeks < 4)
        return weeks + (weeks == 1 ? " tydzień temu" : " tyg temu");
    }
  },
  mounted() {
    this.fetchData();
  },
  computed: {
    ...mapState(["username", "userAvatar", "userId", "isStaff", "accessToken"])
  }
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
  color: rgb(255, 190, 11) !important;
}
.formText{
  overflow: hidden;
  white-space: wrap;
}
</style>
