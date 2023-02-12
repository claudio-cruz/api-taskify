from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Note
        fields = [
            'id', 'user', 'title', 'is_owner', 'profile_id',
            'content', 'created_at', 'updated_at',
            'priority', 'category'
        ]
