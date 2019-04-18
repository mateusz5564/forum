    
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=100, blank=True)
    location = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to="avatars", default="default.png", blank=True)



class Post(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null = True,
    )
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/%Y/%m/%D/")
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
    )
    parent_id = models.ForeignKey('Comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)


class Post_rating(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
    )


class Comment_rating(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    comment = models.OneToOneField(
        Comment,
        on_delete=models.CASCADE,
    )
    is_positive = models.BooleanField(default=True)