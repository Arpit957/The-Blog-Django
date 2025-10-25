from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000000)
    created_at = models.DateTimeField(auto_now_add=True)


