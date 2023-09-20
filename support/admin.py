"""
Admin configuration for managing models in the Django admin site.
This file registers relevant model.
"""

from django.contrib import admin
from .models import *

admin.site.register(Support)
