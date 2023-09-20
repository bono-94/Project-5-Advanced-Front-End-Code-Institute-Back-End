"""
Knowl3dg3 Containers URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include
from .views import root_route

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include ('dj_rest_auth.registration.urls')),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
    path('', include('containers.urls')),
    path('', include('favourites.urls')),
    path('', include('friends.urls')),
    path('', include('support.urls')),
]