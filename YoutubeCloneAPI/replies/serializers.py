from rest_framework import serializers
from .models import Reply


class ReplySeralizer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = [
            'id', 'username',
            'time_posted', 'message', 'likes',
            'dislikes', 'original_post',
        ]
