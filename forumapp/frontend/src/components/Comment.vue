<template>
    <v-container amber accent-2>
        <v-layout>
            <v-flex mr-2 shrink>
                <img 
                :src="comment.avatar_url" 
                alt="obrazek"
                width="40"
                height="40"
                >
            </v-flex>
            <v-flex>
                <span class="black--text subheading font-weight-medium">
                    {{ comment.user.username }} {{ comment.created_at }} <br/>
                </span>

                {{ comment.content }}
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias laboriosam fugit earum necessitatibus deserunt exercitationem voluptate voluptatem delectus, aut quia doloribus veritatis rem modi debitis eos dolore illo, consequatur rerum.
 
                <button>like</button>
                {{ comment.number_of_comment_likes }}
                <button>dislike</button>
                {{ comment.number_of_comment_dislikes }}

                <ChildrenComment v-for="children in comment.children_comments" :key="children.id" :comment="children" />
            </v-flex>
        </v-layout>

    </v-container>
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
    .child_comment_pg {
        width: 51px;
    }
</style>