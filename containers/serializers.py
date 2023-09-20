from rest_framework import serializers
from containers.models import Container
from posts.models import Post


class ContainerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Container
        fields = [
            'id',
            'created_at',
            'owner',
            'is_public',
            'container_name',
            'container_info',
        ]