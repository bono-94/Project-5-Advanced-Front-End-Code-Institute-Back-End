from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to 'owner' and 'followed'.
    'owner' is a User that is following a User.
    'followed' is a User that is followed by 'owner'.
    related_name attribute can differentiate
    between 'owner' and 'followed' who both are User model instances.
    'unique_together' makes sure a user can't 'double follow' the same user.
    """
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE, unique=False
    )
    
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} following {self.followed}'