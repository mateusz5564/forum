from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Profile, Post, Comment, Post_rating, Comment_rating
from django.contrib.auth.models import User
from .serializers import UserAllDetailSerializer, UserDetailSerializer, ProfileSerializer, PostSerializer, CommentSerializer, Post_ratingSerializer, Comment_ratingSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAllDetailSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class Post_ratingView(viewsets.ModelViewSet):
    queryset = Post_rating.objects.all()
    serializer_class = Post_ratingSerializer

class Comment_ratingView(viewsets.ModelViewSet):
    queryset = Comment_rating.objects.all()
    serializer_class = Comment_ratingSerializer



 