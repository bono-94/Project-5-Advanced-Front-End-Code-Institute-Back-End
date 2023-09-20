from rest_framework import generics, permissions
from .models import Support
from .serializers import SupportSerializer
from knowledge.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class SupportList(generics.ListCreateAPIView):
    """
    List support requests or create a new support request if logged in.
    """
    serializer_class = SupportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Support.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['support_type']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SupportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a support request by ID if the user is the owner.
    """
    serializer_class = SupportSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Support.objects.all()