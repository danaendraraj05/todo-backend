from django.db import models
from django.contrib.auth.models import User
from app.models.project import Project

class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assignees = models.ManyToManyField(User, related_name='todo_assignees')
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='todo_attachments/', null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.todo.title}"

