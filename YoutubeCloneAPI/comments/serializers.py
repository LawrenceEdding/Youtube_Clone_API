from rest_framework import serializers
from .models import Comment


class CommentSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 'username',
            'time_posted', 'message', 'likes',
            'dislikes', 'video_id',
        ]
