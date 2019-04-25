<template>
    <div class="comment-wrapper">
        <div class="user-avatar">
            <img :src="comment.avatar_url" alt="obrazek">
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
        <div class='children-comments'>
            <ChildrenComment v-for="children in comment.children_comments" :key="children.id" :comment="children" />
        </div>
    </div>
</template>

<script>
    import ChildrenComment from './ChildrenComment.vue';

    export default {
        props: ['comment'],
            components: {
                ChildrenComment
            },
    }
</script>

<style lang="scss" scoped>
    .comment-wrapper {
        height: auto;
        width: 100%;
        background-color: blueviolet;
        .user-avatar img{
            max-width: 60px;
            max-height: 60px;
        }
        .interaction-buttons {
            display: inline-block;
        }
        .children_comments{
            float: left;
            width: 100%;
            background-color: red;
        }
    }
</style>