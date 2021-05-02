from .models import Reply
from .serializers import ReplySeralizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class ReplyList(APIView):

    def get(self, request):
        song = Reply.objects.all()
        serializer = ReplySeralizer(song, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReplySeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyDetail(APIView):

    def get(self, request, pk):
        reply = self.get_object(pk)
        serializer = ReplySeralizer(reply)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        reply = self.get_object(pk)
        serializer = ReplySeralizer(data=request.data, instance=reply)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404
