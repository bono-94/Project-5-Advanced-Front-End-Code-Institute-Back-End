from django.db import models
from django.contrib.auth.models import User
from containers.models import Container

class Post(models.Model):
    """
    Post model, related to 'owner', a User instance.
    Default image set so that we can always reference image.url.
    """

    post_category_choices = [
        ('announcement', 'Announcement'),
        ('answer', 'Answer'),
        ('blog', 'Blog'),
        ('event', 'Event'),
        ('idea', 'Idea'),
        ('interview', 'Interview'),
        ('journal', 'Journal'),
        ('news', 'News'),
        ('review', 'Review'),
        ('story', 'Story'),
        ('theory', 'Theory'),
        ('tutorial', 'Tutorial'),
        ('question', 'Question'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    containers = models.ManyToManyField(Container)

    post_category = models.CharField(
        max_length=15,
        choices=post_category_choices,
        blank=False,
        default='theory'
    )

    image = models.ImageField(
        upload_to='post_images/',
        default='post_images/tree.jpg',
        blank=True,
        null=True
    )
    
    title = models.CharField(max_length=42, blank=False, unique=True)
    sub_title = models.CharField(max_length=84, blank=False, unique=True)
    topic = models.CharField(max_length=42, blank=False)
    location = models.CharField(max_length=42, blank=False)
    content = models.TextField(max_length=2100, blank=False)
    inspiration = models.CharField(max_length=840, blank=False)
    source = models.CharField(max_length=420, blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Post ({self.id}) by {self.owner.username}'