<template>
    <v-container amber lighten-3>
        <div class="user-avatar">
            <v-img 
            :src="comment.avatar_url"
             alt="obrazek"
             width="40px"
             height="40px"
             ></v-img>
        </div>
        <div class="comment-header">
            {{ comment.user.username }} {{ comment.created_at }}
        </div>
        <div class="comment-content">
            {{ comment.content }}
        </div>
        <div class="interaction-buttons">
            <button>like</button>
            {{ comment.number_of_comment_likes }}
            <button>dislike</button>
            {{ comment.number_of_comment_dislikes }}
        </div>
    </v-container>
</template>

<script>
    export default {
        props: ['comment']
    }
</script>

<style lang="scss" scoped>

</style>