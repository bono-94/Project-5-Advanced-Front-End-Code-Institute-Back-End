from rest_framework import serializers
from .models import Support
from django.contrib.humanize.templatetags.humanize import naturaltime

class SupportSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Support
        fields = [
            'id',
            'owner',
            'is_owner',
            'created_at',
            'support_type',
            'title',
            'content',
            'container_name',
            'knowledge_name',
        ]