from rest_framework import serializers
from .models import Comment


class CommentSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 'username',
            'time_posted', 'message', 'times_liked'
            'times_disliked', 'video_id',
        ]