from django.db import models
from common.models import CommonModel
from comments.models import Comment


class Reply (CommonModel):
    original_post = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        ordering = ["time_posted"]
