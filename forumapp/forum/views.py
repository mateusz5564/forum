from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Profile, Post, Comment, Post_rating, Comment_rating
from django.contrib.auth.models import User
from .serializers import CommentRatingSerializer, PostRatingSerializer, UserAllDetailSerializer, UserDetailSerializer, ProfileSerializer, PostSerializer, CommentSerializer, Post_ratingSerializer, Comment_ratingSerializer, PostCommentSerializer, PostMemeSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAllDetailSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user__username',)

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user__username', 'id')
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(parent_id__isnull=True)
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user__username', 'id')

class Post_ratingView(viewsets.ModelViewSet):
    queryset = Post_rating.objects.all()
    serializer_class = Post_ratingSerializer

class Comment_ratingView(viewsets.ModelViewSet):
    queryset = Comment_rating.objects.all()
    serializer_class = Comment_ratingSerializer


#POST
class CommentCreateAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = PostCommentSerializer


class PostCreateAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostMemeSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Post.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

class PostRatingCreateAPIView(viewsets.ModelViewSet):
    queryset = Post_rating.objects.all()
    serializer_class = PostRatingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'post')

class CommentRatingCreateAPIView(viewsets.ModelViewSet):
    queryset = Comment_rating.objects.all()
    serializer_class = CommentRatingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'comment')

 