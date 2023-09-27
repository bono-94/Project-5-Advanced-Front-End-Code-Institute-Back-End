from rest_framework import generics, permissions
from .models import Container
from .serializers import ContainerSerializer
from knowledge.permissions import IsOwnerOrReadOnly


class ContainerList(generics.ListCreateAPIView):
    """
    List containers or create a container if logged in.
    """
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ContainerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a container and edit or delete it if you own it.
    """
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    permission_classes = [IsOwnerOrReadOnly]

class PublicContainerList(generics.ListAPIView):
    queryset = Container.objects.filter(is_public=True)
    serializer_class = ContainerSerializer

class PrivateContainerList(generics.ListAPIView):
    queryset = Container.objects.filter(is_public=False)
    serializer_class = ContainerSerializer