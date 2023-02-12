from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer
from api_taskify.permissions import IsOwner


class NoteList(generics.ListCreateAPIView):
    """
    List all notes owned by the authenticated user.
    Create new notes.
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(user=self.request.user)
        else:
            return Note.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a note instance if user is the owner.
    """
    permission_classes = [IsOwner]
    serializer_class = NoteSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(user=self.request.user)
        else:
            return Note.objects.none()
