from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_profile(models.Model):
    user : models.ForeignKey(User, on_delete=models.CASCADE)
    age: models.IntegerField()
    description : models.TextField()
