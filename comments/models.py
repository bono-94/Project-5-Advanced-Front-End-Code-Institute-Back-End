from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.utils.timesince import timesince


class Comment(models.Model):
    """
    Comment model that leaves user input on posts.
    Externally related to User and Post models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
   
    title = models.CharField(max_length=42, blank=False, unique=True)
    content = models.TextField(max_length=420, blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content