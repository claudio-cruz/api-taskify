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


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='other')

    class Meta:
        ordering = ['-due_date', 'priority']

    def __str__(self):
        return f'{self.id} {self.task}'
