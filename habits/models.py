from django.db import models
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

FREQUENCY_CHOICES = [
        ('daily', 'Everyday'),
        ('six times a week', 'Six times a week'),
        ('five times a week', 'Five times a week'),
        ('four times a week', 'Four times a week'),
        ('three times a week', 'Three times a week'),
        ('two times a week', 'Two times a week'),
        ('ones a week', 'Ones a week'),
    ]


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    time = models.TimeField(blank=True)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    class Meta:
        ordering = ['time', 'priority']

    def __str__(self):
        return f'{self.id} {self.title}'
