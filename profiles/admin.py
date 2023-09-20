"""
Admin configuration for managing models in the Django admin site.
This file registers relevant model and customizes the admin interface.
"""

from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Profile)
