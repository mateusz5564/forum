from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('profiles', views.ProfileView)
router.register('posts', views.PostView)
router.register('comments', views.CommentView)
router.register('posts_rating', views.Post_ratingView)
router.register('comment_rating', views.Comment_ratingView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]