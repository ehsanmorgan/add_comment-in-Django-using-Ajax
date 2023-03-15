from rest_framework import generics
from .sserializer import postSerializer,postDetailSerializer,CommentSerializer
from .models import Post,Comment


class postListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=postSerializer
    
    
class postDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=postDetailSerializer
    lookup_field='slug'
    
    
class CommentListApi(generics.ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    