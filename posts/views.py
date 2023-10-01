from rest_framework import generics, permissions, filters
from knowledge.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from .models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        favourites_count=Count('favourites', distinct=True),
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        containers_count=Count('containers', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'favourites__owner__profile',
        'owner__profile',
        'containers',
    ]

    search_fields = [
        'owner__username',
        'title',
        'sub_title',
        'post_category',
        'topic',
        'content',
    ]
    
    ordering_fields = [
        'favourites_count',
        'likes_count',
        'comments_count',
        'containers_count',
        'likes__created_at',
        'favourites__created_at'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        favourites_count=Count('favourites', distinct=True),
        comments_count=Count('comment', distinct=True),
        containers_count=Count('containers', distinct=True)
    ).order_by('-created_at') 