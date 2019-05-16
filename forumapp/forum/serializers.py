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
    avatar_url = serializers.SerializerMethodField('get_avatar_url2')

    class Meta:
        model = Comment
        fields = ('user', 'content', 'created_at', 'avatar_url')

    def get_avatar_url2(self, obj):
        return "http://127.0.0.1:8000/media/{}".format(obj.user.profil.avatar)     

class CommentSerializer(serializers.ModelSerializer):
    user = UserAllDetailSerializer()
    comment_likes = Comment_ratingSerializer(many=True)
    children_comments = Children_comentSerializer(many=True)
    number_of_comment_likes = serializers.SerializerMethodField()
    number_of_comment_dislikes = serializers.SerializerMethodField()
    avatar_url = serializers.SerializerMethodField('get_avatar_url2')

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'avatar_url',
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

    def get_avatar_url2(self, obj):
        return "http://127.0.0.1:8000/media/{}".format(obj.user.profil.avatar)    

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
    number_of_comments = serializers.SerializerMethodField()

    

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
            'number_of_post_likes',
            'number_of_comments'
            )

    def get_number_of_post_likes(self, obj):
        return obj.post_likes.count()

    def get_number_of_comments(self, obj):
        return obj.comments.count()

    def get_comments_no_parent_id(self, post):
        qs = Comment.objects.filter(parent_id__isnull=True, post=post)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data


#POST
class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostMemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'