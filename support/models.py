from django.db import models
from django.contrib.auth.models import User


class Support(models.Model):
    """
    Support model, related to 'owner', a User instance.
    """
    support_type_choices = [
        ('consultacy', 'Book a Consultancy'),
        ('feedback', 'Feedback'),
        ('request', 'Request Knowledge'),
        ('support', 'Support Ticket'),
        ('suggestion', 'Suggestion')        
    ]

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    support_type = models.CharField(
        max_length=21,
        choices=support_type_choices,
        blank=False,
        default='support'
    )

    title = models.CharField(max_length=84, blank=False)
    content = models.TextField(max_length=2100, blank=False)

    container_name = models.CharField(max_length=42, blank=True, null=True)
    knowledge_name = models.CharField(max_length=42, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} - {self.title}'