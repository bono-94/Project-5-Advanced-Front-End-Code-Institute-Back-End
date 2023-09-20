from django.db import models
from django.contrib.auth.models import User


class Container(models.Model):
    """
    Container model, related to User and Post
    """
    created_at = models.DateTimeField(auto_now_add=True)
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    is_public = models.BooleanField(default=True)

    container_name = models.CharField(max_length=42, blank=False)
    container_info = models.TextField(max_length=420, blank=False)
    
    class Meta:
        ordering = ['container_name']

    def __str__(self):
        return self.container_name