from django.contrib import admin
from .models import Profile, Post, Post_rating, Comment, Comment_rating

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Post_rating)
admin.site.register(Comment_rating)
# Register your models here.
