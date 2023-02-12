from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

CATEGORY_CHOICES = [
    ('other', 'Other'),
    ('study', 'Study'),
    ('finance', 'Finance'),
    ('work', 'Work'),
    ('sport', 'Sport'),
    ('social', 'Social'),
    ('home', 'Home'),
]

REPEAT_CHOICES = [
        ('none', 'No repeat'),
        ('daily', 'Everyday'),
        ('weekly', 'Once a Week'),
        ('monthly', 'Once a Month'),
        ('yearly', 'Once a Year'),
    ]


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)
    repeat = models.CharField(
        max_length=10, choices=REPEAT_CHOICES, default='none'
        )
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default='medium'
        )
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default='other'
        )

    class Meta:
        ordering = ['-start_time', 'priority']

    def __str__(self):
        return f'{self.id} {self.event}'


def create_event(sender, instance, created, **kwargs):
    if created:
        Event.objects.create(user=instance)


post_save.connect(create_event, sender=User)
