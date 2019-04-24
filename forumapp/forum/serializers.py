from rest_framework import serializers
from .models import Profile, Post, Comment, Post_rating, Comment_rating
from django.contrib.auth.models import User


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'last_login', 'date_joined')

class ProfileSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar',)


class UserAllDetailSerializer(serializers.ModelSerializer):
    profil = ProfileSerializer2()

    class Meta:
        model = User
        fields = ('id', 'username', 'profil')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Profile
        fields = '__all__'

class Comment_ratingSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Comment_rating
        fields = '__all__'

class Children_comentSerializer(serializers.ModelSerializer):
    user = UserAllDetailSerializer()

    class Meta:
        model = Comment
        fields = ('user', 'content', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    user = UserAllDetailSerializer()
    comment_likes = Comment_ratingSerializer(many=True)
    children_comments = Children_comentSerializer(many=True)
    number_of_comment_likes = serializers.SerializerMethodField()
    number_of_comment_dislikes = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'content',
            'created_at',
            'comment_likes',
            'number_of_comment_likes',
            'number_of_comment_dislikes',
            'parent_id',
            'children_comments'
        )

    def get_number_of_comment_likes(self, obj):
        return obj.comment_likes.count()

    def get_number_of_comment_dislikes(self, obj):
        return obj.comment_likes.filter(is_positive=False).count()

class Post_ratingSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Post_rating
        fields = '__all__'


#Serializer tworzący API dla listy postów
class PostSerializer(serializers.ModelSerializer):
    user = UserAllDetailSerializer()
    # comments = CommentSerializer(many=True)
    post_likes = Post_ratingSerializer(many=True)
    comments = serializers.SerializerMethodField('get_comments_no_parent_id')
    number_of_post_likes = serializers.SerializerMethodField()

    

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'created_at', 
            'image', 
            'text', 
            'user', 
            'comments', 
            'post_likes', 
            'number_of_post_likes'
            )

    def get_number_of_post_likes(self, obj):
        return obj.post_likes.count()

    def get_comments_no_parent_id(self, post):
        qs = Comment.objects.filter(parent_id__isnull=True, post=post)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data

