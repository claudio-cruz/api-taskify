from django.db import models
from django.contrib.auth.models import User

PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

CATEGORY_CHOICES = [
    ('study', 'Study'),
    ('finance', 'Finance'),
    ('work', 'Work'),
    ('sport', 'Sport'),
    ('social', 'Social'),
    ('home', 'Home'),
    ('other', 'Other'),
]

REPEAT_CHOICES = [
        ('daily', 'Everyday'),
        ('weekly', 'Once a Week'),
        ('monthly', 'Once a Month'),
        ('yearly', 'Once a Year'),
        ('none', 'No repeat'),
    ]


class Event(models.Model):
    name = models.CharField(max_length=100)
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
