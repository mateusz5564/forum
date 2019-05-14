<template>
  <v-layout mb-3 mt-3>
    <v-flex mr-3 shrink>
      <img :src="comment.avatar_url" alt="obrazek" width="40" height="40">
    </v-flex>

    <v-flex>
      <v-layout justify-space-between row>
        <v-flex shrink>
          <span class="black--text subheading font-weight-medium">{{ comment.user.username }}</span>
          <span class="caption"> {{ calculateDate(comment.created_at) }} </span>
        </v-flex>

        <v-flex shrink>
          <v-btn class="rew-btn" flat icon color="black">
            <v-icon>add_circle</v-icon>
          </v-btn>
          0
            <!-- {{ mark(comment.number_of_comment_likes, comment.number_of_comment_dislikes) }} -->
          <v-btn class="rew-btn" flat icon color="black">
            <v-icon>remove_circle</v-icon>
          </v-btn>
        </v-flex>
      </v-layout>

      <v-layout>
        <v-flex>{{ comment.content }}</v-flex>
      </v-layout>

    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: ["comment"],
  methods: {
    mark: function(likes, dislikes) {
      return (likes - dislikes)
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
       if (hours < 59) return hours + (hours == 1 ? " godzinę temu" : " godz temu");
       if (days < 7) return days + (days == 1 ? " dzień temu" : " dni temu");
       if (weeks < 4) return weeks + (weeks == 1 ? " tydzień temu" : " tyg temu");
    }
  },
};
</script>

<style lang="scss" scoped>
.rew-btn {
  margin: 0;
}
</style>
