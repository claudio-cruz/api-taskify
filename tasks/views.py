from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from api_taskify.permissions import IsOwner


class TaskList(generics.ListCreateAPIView):
    """
    List all tasks, create new tasks.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a task instance.
    """
    permission_classes = [IsOwner]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
