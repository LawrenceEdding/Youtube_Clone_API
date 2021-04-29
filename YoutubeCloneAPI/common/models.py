from django.db import models
from datetime import datetime


# Create your models here.
class CommonModel(models.Model):
    username = models.CharField(max_length=50)
    time_posted = models.DateTimeField(default=datetime.now())
    message = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
