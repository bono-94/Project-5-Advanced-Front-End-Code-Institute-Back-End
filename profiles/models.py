from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    
    image = models.ImageField(
        upload_to='images/', default='../default_profile_qdjgyp'
    )
    

    first_name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    age = models.IntegerField()
    bio = models.TextField(blank=True)
    # Contact
    # Social media


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
