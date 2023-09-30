from rest_framework import serializers
from containers.models import Container
from posts.models import Post


class ContainerSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Container
        fields = [
            'id',
            'created_at',
            'owner',
            'is_owner',
            'is_public',
            'container_name',
            'container_info',
            'profile_id',
            'profile_image'
        ]

class ContainerSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ['id', 'container_name', 'container_info']