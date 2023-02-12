from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from api_taskify.permissions import IsOwner


class ProfileList(generics.ListAPIView):
    """
    List the profile of the currently authenticated user.
    """
    serializer_class = ProfileSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Profile.objects.filter(user=self.request.user)
        else:
            return Profile.objects.none()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update the profile of the currently authenticated user.
    """
    permission_classes = [IsOwner]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Profile.objects.filter(user=self.request.user)
        else:
            return Profile.objects.none()
