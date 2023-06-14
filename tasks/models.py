from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

class TaskGroup(models.Model):
    title = models.CharField(max_length=200)
    class Meta:
        app_label = 'tasks'

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks')
    task_group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, related_name='tasks')
    class Meta:
        app_label = 'tasks'
