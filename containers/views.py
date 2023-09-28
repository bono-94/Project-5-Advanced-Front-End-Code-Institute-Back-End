from rest_framework import generics, permissions, filters
from .models import Container
from .serializers import ContainerSerializer, ContainerSearchSerializer
from knowledge.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ContainerList(generics.ListCreateAPIView):
    """
    List containers or create a container if logged in.
    """
    queryset = Container.objects.filter(is_public=False)
    serializer_class = ContainerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'is_public',                  # Add fields you want to filter on
    ]

    search_fields = [
        'owner__username',
        'container_name',             # Add fields you want to search on
        'container_info',                # Add other fields you want to search on
    ]

    ordering_fields = [
        'created_at',                 # Add fields you want to enable ordering on
        'container_name',             # Add other fields you want to enable ordering on
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ContainerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a container and edit or delete it if you own it.
    """
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PublicContainerList(generics.ListAPIView):
    queryset = Container.objects.filter(is_public=True)
    serializer_class = ContainerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'is_public',                  # Add fields you want to filter on
    ]

    search_fields = [
        'owner__username',
        'container_name',             # Add fields you want to search on
        'container_info',                # Add other fields you want to search on
    ]

    ordering_fields = [
        'created_at',                 # Add fields you want to enable ordering on
        'container_name',             # Add other fields you want to enable ordering on
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PrivateContainerList(generics.ListAPIView):
    queryset = Container.objects.filter(is_public=False)
    serializer_class = ContainerSerializer
    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'is_public',                  # Add fields you want to filter on
    ]

    search_fields = [
        'owner__username',
        'container_name',             # Add fields you want to search on
        'container_info',                # Add other fields you want to search on
    ]

    ordering_fields = [
        'created_at',                 # Add fields you want to enable ordering on
        'container_name',             # Add other fields you want to enable ordering on
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ContainerSearch(generics.ListAPIView):
    serializer_class = ContainerSearchSerializer

    def get_queryset(self):
        query = self.request.query_params.get('search', '')
        return Container.objects.filter(is_public=True, container_name__icontains=query)