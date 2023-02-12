from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Event
        fields = [
            'id', 'user', 'event', 'is_owner', 'profile_id',
            'start_time', 'end_time', 'description',
            'repeat', 'priority', 'category'
        ]
