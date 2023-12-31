from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from favourites.models import Favourite
from containers.serializers import ContainerSerializer
from containers.models import Container


class PostSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    favourite_id = serializers.SerializerMethodField()
    favourites_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    containers_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 4:
            raise serializers.ValidationError(
                'Image size larger than 4MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_favourite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                owner=user, post=obj
            ).first()
            return favourite.id if favourite else None
        return None

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'containers',
            'post_category',
            'image',
            'title',
            'sub_title',
            'topic',
            'location',
            'content', 
            'inspiration',
            'source',
            'favourite_id',
            'favourites_count',
            'like_id',
            'likes_count',
            'comments_count',
            'containers_count',
        ]
