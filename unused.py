from django.http import Http404
from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from knowledge.permissions import IsOwnerOrReadOnly

# Create your views here.

class PostList(APIView):
    """
    List posts or create a post if logged in
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

# Create your views here.
class PostDetail(APIView):
    """
    Retrieve a post and edit or delete it if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer

    def get_object(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from knowledge.permissions import IsOwnerOrReadOnly


class ProfileList(APIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many=True, context={'request': request}
        )
        return Response(serializer.data)


class ProfileDetail(APIView):
    
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
