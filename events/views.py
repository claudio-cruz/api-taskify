from rest_framework import generics, permissions, filters
from .models import Event
from .serializers import EventSerializer
from api_taskify.permissions import IsOwner


class EventList(generics.ListCreateAPIView):
    """
    List all events owned by the authenticated user.
    Create new events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = [
        'event', 'description', 'start_time', 'priority', 'category'
        ]
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Event.objects.filter(user=self.request.user)
        else:
            return Event.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a event instance if user is the owner.
    """
    permission_classes = [IsOwner]
    serializer_class = EventSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Event.objects.filter(user=self.request.user)
        else:
            return Event.objects.none()
