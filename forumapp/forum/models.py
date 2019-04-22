    
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def user_path(instance, filename):
    return 'avatar/%s/%s' % (instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=100, blank=True)
    location = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to=user_path, default="/avatar/default.jpg", blank=True)

    def __str__(self):
        return self.user.username



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='post_images/%Y/%m/%d/')
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "user: " + self.user.username + " | post_id: " + str(self.id)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    parent_id = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)

    def __str__(self):
        result = "user: " + self.user.username + " | comment_id: " + str(self.id)
        if self.parent_id:
            result += " | parent_id: " + str(self.parent_id.id)
        return result


class Post_rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return "user: " + self.user.username + " | post_id: " + str(self.post.id)

class Comment_rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    is_positive = models.BooleanField(default=True)

    def __str__(self):
        return "user: " + self.user.username + " | comment_id: " + str(self.comment.id)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def post_save_receiver(sender, instance, **kwargs):
    instance.profile.save()    


        
    