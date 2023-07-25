from rest_framework import generics, permissions, filters
from .models import Habit
from .serializers import HabitSerializer
from api_taskify.permissions import IsOwner


class HabitList(generics.ListCreateAPIView):
    """
    List all habits owned by the authenticated user.
    Create new habits.
    """
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = [
        'title', 'description', 'frequency', 'priority', 'category'
        ]
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Habit.objects.filter(user=self.request.user)
        else:
            return Habit.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a habit instance if user is the owner.
    """
    permission_classes = [IsOwner]
    serializer_class = HabitSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Habit.objects.filter(user=self.request.user)
        else:
            return Habit.objects.none()
