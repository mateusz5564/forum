<template>
    <div class="comment-wrapper">
        <div class="user-avatar">
            <img :src="post.user.profil.avatar" alt="obrazek">
        </div>
        <div class="comment-header">
            {{ post.username }} {{ post.created_at }}
        </div>
        <div class="comment-content">
            {{ post.text }}
        </div>
        <div class="interaction-buttons">
            <button>like</button>
            {{ post.comments.number_of_comment_likes }}
            <button>dislike</button>
            {{ post.comments.number_of_comment_dislikes }}
        </div>
    </div>
</template>

<script>
    export default {
        props: ['post']
    }
</script>

<style lang="scss" scoped>
    .comment-wrapper {
        height: 100px;
        width: 100%;
        background-color: blueviolet;
        .user-avatar img{
            max-width: 60px;
            max-height: 60px;
        }
        .interaction-buttons {
            display: inline-block;
        }
    }
</style>