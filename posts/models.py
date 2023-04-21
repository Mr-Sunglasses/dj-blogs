import datetime

from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title: str = models.CharField(max_length=25)
    body: str = models.CharField(max_length=500)
    author: str = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    time: str = models.DateTimeField(default=now())

    def __str__(self):
        return f"TITLE: {self.title} || POST: {self.body[0:30]}"