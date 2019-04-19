from rest_framework import serializers
from .models import Profile, Post, Comment, Post_rating, Comment_rating
from django.contrib.auth.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'last_login', 'date_joined')

class UserAllDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Post
        fields = '__all__'


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'location', 'avatar')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class Post_ratingSerializer(serializers.HyperlinkedModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Post_rating
        fields = '__all__'

class Comment_ratingSerializer(serializers.HyperlinkedModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Comment_rating
        fields = '__all__'