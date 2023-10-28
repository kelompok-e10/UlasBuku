from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Forum(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forums")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class User(models.Model):
    name = models.CharField(max_length=64)
    forums = models.ManyToManyField(Forum, blank=True, related_name="users")

