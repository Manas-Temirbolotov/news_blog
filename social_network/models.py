from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    objects = None
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

