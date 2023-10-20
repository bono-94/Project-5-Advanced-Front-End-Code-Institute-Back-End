from rest_framework import generics, permissions, filters
from .models import Container
from .serializers import ContainerSerializer
from knowledge.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

class ContainerList(generics.ListCreateAPIView):
    """
    List containers or create a container if logged in.
    """
    serializer_class = ContainerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'is_public',                  
    ]

    search_fields = [
        'owner__username',
        'container_name',             
        'container_info',                
    ]

    ordering_fields = [
        'created_at',                 
        'container_name',  
        'owner__username'           
    ]

    def get_queryset(self):
        user = self.request.user

        queryset = Container.objects.filter(Q(is_public=True) | (Q(is_public=False) & Q(owner=user)))

        return queryset

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
        'container_info'               # Add other fields you want to search on
    ]

    ordering_fields = [
        'created_at',                 # Add fields you want to enable ordering on
        'container_name',             # Add other fields you want to enable ordering on
        'owner__username'
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
        'is_public',                
    ]

    search_fields = [
        'owner__username',
        'container_name',            
        'container_info',                
    ]

    ordering_fields = [
        'created_at',                 
        'container_name',   
        'owner__username'         
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
