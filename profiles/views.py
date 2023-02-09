from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from api_taskify.permissions import IsOwner


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if user is the owner.
    """
    permission_classes = [IsOwner]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
