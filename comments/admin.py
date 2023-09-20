# """
# Admin configuration for managing models in the Django admin site.
# This file registers models and customizes the admin interface.
# """

# from django.contrib import admin
# from .models import Post, Note, Profile
# from django_summernote.admin import SummernoteModelAdmin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin


# # NOTES ADMIN
# @admin.register(Note)
# class NotesAdmin(admin.ModelAdmin):

#     list_display = ('content_note', 'note', 'created_on_note', 'approved')
#     list_filter = ('content_note', 'note', 'approved', 'created_on_note')
#     search_fields = ('content_note', 'email', 'content_note')

#     # ACTIONS
#     actions = ['approved_note']

#     def approved_note(self, request, queryset):
#         queryset.update(approved=True)

