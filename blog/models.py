from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.PositiveIntegerField(default=int(datetime.now().timestamp()))
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.PositiveIntegerField(default=int(datetime.now().timestamp()))

    def __str__(self):
        return self.content
