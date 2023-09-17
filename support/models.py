from django.db import models
from django.contrib.auth.models import User

class Support(models.Model):
    """
    Support model, related to 'owner', i.e. a User instance.
    """
    support_type_choices = [
        ('request', 'Request Knowledge'),
        ('consultacy', 'Book a Consultancy'),
        ('support', 'Support Ticket'),
        ('blog', 'Blog'),
    ]
    status = [
        ('open', 'Open'),
        ('closed', 'Closed')
    ]

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    support_type = models.CharField(
        max_length=32,
        choices=support_type_choices, default='idea'
    )

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    support_ticket = models.IntegerField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    # datetime
    # main question for consultancy
    # content vs functional support


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

    # How long ago validation