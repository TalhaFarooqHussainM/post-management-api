from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import Post

from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def ShowPost(self, request):
        results = Post.objects.all()
        serializer  = PostSerializer(results, many=True)
        return Response(serializer .data)


    def SavePost(self, request):
        serializer  = PostSerializer(data=request.data)
        if serializer .is_valid():
            serializer .save()
            return Response(serializer .data, status=status.HTTP_201_CREATED)
        return Response(serializer .data, status=status.HTTP_400_BAD_REQUEST)
