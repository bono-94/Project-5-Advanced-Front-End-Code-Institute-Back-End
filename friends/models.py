from django.db import models
from django.contrib.auth.models import User

class Friend(models.Model):
    """
    Friend model, related to 'owner' and 'requested'.
    'owner' is a User that is requesting a friendship with other User.
    'requested' is a User that is receiving request by 'owner'.
    We need the related_name attribute so that django can differentiate.
    between 'owner' and 'requested' who both are User model instances.
    'unique_together' makes sure a user can't 'double follow' the same user.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    
    owner = models.ForeignKey(
        User, related_name='friends', on_delete=models.CASCADE
    )
    requested = models.ForeignKey(
        User, related_name='requested', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'requested']

    def __str__(self):
        return f'{self.owner} {self.requested}'
