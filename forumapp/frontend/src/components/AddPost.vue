<template>
  <v-container grey mb-5>
    <v-layout>
      <v-flex xs12>
        <v-text-field v-model="title" label="Tytuł" background-color="grey lighten-3" solo flat></v-text-field>
      </v-flex>
    </v-layout>

    <v-layout>
      <v-flex xs12 class="text-xs-center">
        <v-text-field
          label="Wybierz obraz"
          @click="pickFile"
          v-model="imageName"
          prepend-icon="add_photo_alternate"
        ></v-text-field>
        <input
          type="file"
          style="display: none"
          ref="image"
          accept="image/*"
          @change="onFilePicked"
        >
      </v-flex>
    </v-layout>

    <v-layout>
      <v-flex xs12>
        <v-textarea v-model="text" box label="Tekst" value></v-textarea>
      </v-flex>
    </v-layout>

    <v-layout justify-center mb-4>
      <v-flex shrink>
        <img :src="imageUrl" width="100%" v-if="imageUrl">
      </v-flex>
    </v-layout>

    <v-layout justify-center>
      <v-flex sm2>
        <v-btn color="amber" class="black--text" @click="postMeme()">Dodaj</v-btn>
      </v-flex>

      <v-flex sm2>
        <v-btn class="black--text">Anuluj</v-btn>
      </v-flex>
    </v-layout>

    <v-dialog v-model="dialog" max-width="290">
      <v-card>
        <v-card-title class="headline green--text darken-1">Dodano post!</v-card-title>
        <!-- <v-card-text>test</v-card-text> -->
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat="flat" @click.native="dialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
  data: () => ({
    title: null,
    text: null,
    image: null,
    isAccepted: null,
    dialog: false,
    imageName: "",
    imageUrl: "",
    imageFile: ""
  }),

  methods: {
    pickFile() {
      this.$refs.image.click();
    },
    onFilePicked(e) {
      const files = e.target.files;
      if (files[0] !== undefined) {
        this.imageName = files[0].name;
        this.imageFile = e.target.files[0];
        if (this.imageName.lastIndexOf(".") <= 0) {
          return;
        }
        const fr = new FileReader();
        fr.readAsDataURL(files[0]);
        fr.addEventListener("load", () => {
          this.imageUrl = fr.result;
          this.imageFile = files[0];
        });
      } else {
        this.imageName = "";
        this.imageFile = "";
        this.imageUrl = "";
      }
    },
    postMeme() {
      const fd = new FormData();
      fd.append("image", this.imageFile, this.imageFile.name);
      fd.append("title", this.title);
      fd.append("user", this.userId);
      axios.post("http://127.0.0.1:8000/api/post/create/", fd)
        .then(response => {
          this.expand = false;
          this.dialog = !this.dialog;
          // this.fetchData();
        })
        .catch(e => {
          console.error(e);
        });
    }
  },
  computed: {
    ...mapState(["username", "userAvatar", "userId"])
  }
};
</script>

<style lang="scss" scoped>
.container {
  max-width: 650px;
}
</style>