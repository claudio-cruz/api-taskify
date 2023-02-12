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


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    class Meta:
        ordering = ['-due_date', 'priority']

    def __str__(self):
        return f'{self.id} {self.task}'


def create_task(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(user=instance)


post_save.connect(create_task, sender=User)
