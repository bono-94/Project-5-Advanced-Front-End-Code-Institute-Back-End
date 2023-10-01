from django.db.models import Count
from rest_framework import generics, filters, permissions
from knowledge.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        containers_count=Count('owner__container', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
       filters.OrderingFilter,
       filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile',
    ]

    search_fields = [
        'owner__username',
        'profile_quote',
        'first_name',             
        'location',
        'age',
        'bio',
        'website',                
    ]

    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'containers_count',
        'owner__following__created_at',
        'owner__followed__created_at',
        'created_at',
        'updated_at',
        'age',
        'first_name',
        'location',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.[p]
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        containers_count=Count('owner__container', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
