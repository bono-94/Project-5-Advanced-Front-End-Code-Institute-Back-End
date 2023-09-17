from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profiles'
    fk_name = 'username'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# PROFILE ADMIN
@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'username',
        'public_email',
        'location',
        'organization',
        'occupation',
    )
    search_fields = [
        'first_name',
        'last_name',
        'username',
        'public_email',
        'location',
        'organization',
        'occupation',
    ]
    prepopulated_fields = {'slug': ('username',)}
    list_filter = (
        'first_name',
        'last_name',
        'username',
        'public_email',
        'location',
        'organization',
        'occupation',
    )
    summernote_fields = ('bio',)
