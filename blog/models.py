from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=32)
    title = models.CharField(max_length=32, unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
