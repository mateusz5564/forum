<template>
  <v-content>
    <router-view></router-view>

    <v-container class="size">
      <v-layout>
        <v-flex mb-4>
          <div class="text-xs-center">
            <v-btn color="black" outline @click="showAdd = !showAdd">
              <v-icon left>input</v-icon>
              Dodaj post
            </v-btn>
          </div>
        </v-flex>
      </v-layout>
      <v-layout>
        <v-flex v-if="accessToken" v-show="showAdd">
        <v-expand-transition>
          <div v-show="showAdd">
            <AddPost/>
          </div>
        </v-expand-transition>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex>
          <Post v-for="post in posts" :key="post.id" :post="post"></Post>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
import { mapState } from "vuex";
import Post from "../components/Post.vue";
import AddPost from "../components/AddPost.vue";
import axios from "axios";
import { bus } from "../main";
const API = "http://127.0.0.1:8000/api/";

export default {
  name: "app",
  components: {
    Post,
    AddPost
  },
  data() {
    return {
      posts: [],
      showAdd: false
    };
  },
  mounted() {
    axios.get(`${API}posts/?is_accepted=false`).then(response => {
      this.posts = response.data;
    });

    bus.$on("updatePosts", () => {
      this.fetchData();
    });

  },
  methods: {
    fetchData() {
      axios.get(`${API}posts/?is_accepted=false`).then(response => {
      this.posts = response.data;
    });
    }
  },
  computed: {
    ...mapState(["accessToken"])
  }
};
</script>

<style lang="scss">
.size {
  max-width: 700px;
}
</style>
