from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Favourite(models.Model):
    """
    Favourites model, related to User and Post
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        related_name='favourites',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'

    # How long ago validation
