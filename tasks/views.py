from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from api_taskify.permissions import IsOwner


class TaskList(generics.ListCreateAPIView):
    """
    List all tasks owned by the authenticated user.
    Create new tasks.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user)
        else:
            return Task.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a task instance if user is the owner.
    """
    permission_classes = [IsOwner]
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user)
        else:
            return Task.objects.none()
