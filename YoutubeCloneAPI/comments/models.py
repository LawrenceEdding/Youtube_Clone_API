from django.db import models
from common.models import CommonModel
# Create your models here.


class Comment (CommonModel):
    video_id = models.CharField(max_length=50)

    class Meta:
        ordering = ["times_liked"]
