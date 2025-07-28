from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects', null=True)
    assignees = models.ManyToManyField(User, related_name='project_assignees')
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title