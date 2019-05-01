<template>
        <v-layout mt-4>
            <v-flex grey darken-2 pl-1 mr-1></v-flex>
            <v-flex mr-3 shrink>
                <img 
                :src="comment.avatar_url" 
                alt="obrazek"
                width="40"
                height="40"
                >
            </v-flex>
            <v-flex>
                <span class="grey--text--lighten-1 subheading font-weight-medium">
                    {{ comment.user.username }} {{ comment.created_at }} <br/>
                </span>

                {{ comment.content }}
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias laboriosam fugit earum necessitatibus deserunt exercitationem voluptate voluptatem delectus, aut quia doloribus veritatis rem modi debitis eos dolore illo, consequatur rerum.
 
                <button>like</button>
                {{ comment.number_of_comment_likes }}
                <button>dislike</button>
                {{ comment.number_of_comment_dislikes }}
            </v-flex>
        </v-layout>
</template>

<script>
    export default {
        props: ['comment']
    }
</script>

<style lang="scss" scoped>

</style>