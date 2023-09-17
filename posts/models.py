from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    post_type_choices = [
        ('idea', 'Idea'),
        ('story', 'Story'),
        ('journal', 'Journal'),
        ('blog', 'Blog'),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # public_id

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # containers multiple

    # private vs public

    post_type = models.CharField(
        max_length=32,
        choices=post_type_choices, default='idea'
    )
    # topic
    # category
    # keywoards
    # theory or procedure

    folder_upload
    file_upload
    # image, video, audio, document
    # doc, pdf,zip,xcl, csv, parquet

    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    
    title = models.CharField(max_length=255)
    subtitle
    # summary
    content = models.TextField(blank=True)

    # processes
    # activities
    # tasks
    # steps
    # methods




    # inspiration
    # source
   

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

    # How long ago validation
