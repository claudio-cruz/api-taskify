from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../user-icon_pdzqa4')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        if not Profile.objects.filter(email=email).exists():
            Profile.objects.create(user=instance, email=email)


post_save.connect(create_profile, sender=User)
