from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tags'
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title