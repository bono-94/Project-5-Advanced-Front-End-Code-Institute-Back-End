from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    
    image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        default='profile_images/avatar.jpg'
    )
    
    profile_quote = models.CharField(max_length=84, blank=True, null=True)

    first_name = models.CharField(max_length=42, blank=True, null=True)
    location = models.CharField(max_length=42, blank=True, null=True)
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0, "Age cannot be negative."),
            MaxValueValidator(121,  "Age must be 120 or less.")
        ],
        null=True,
        blank=True
    )
    bio = models.TextField(max_length=210, blank=True, null=True)

    website = models.URLField(
        max_length=210,
        unique=True,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)

