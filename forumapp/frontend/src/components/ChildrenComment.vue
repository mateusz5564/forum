<template>
    <div class="comment-wrapper">
        <div class="user-avatar">
            <img :src="comment.user.profil.avatar" alt="obrazek">
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
    </div>
</template>

<script>
    export default {
        props: ['comment']
    }
</script>

<style lang="scss" scoped>
    .comment-wrapper {
        height: auto;
        width: 100%;
        background-color: red;
        .user-avatar img{
            max-width: 60px;
            max-height: 60px;
        }
        .interaction-buttons {
            display: inline-block;
        }
    }
</style>