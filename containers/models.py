from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Container(models.Model):
    """
    Container model, related to User and Post
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    description = models.TextField()
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

    # How long ago validation