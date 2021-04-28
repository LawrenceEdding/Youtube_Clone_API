from django.db import models


# Create your models here.
class CommonModel(models.Model):
    username = models.CharField(max_length=50)
    time_posted = models.DateTimeField()
    message = models.TextField()
    times_liked = models.PositiveIntegerField()
    times_disliked = models.PositiveIntegerField()

    class Meta:
        abstract = True
