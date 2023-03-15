from rest_framework import generics
from .sserializer import postSerializer,postDetailSerializer
from .models import Post


class postListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=postSerializer
    
    
class postDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=postDetailSerializer
    lookup_field='slug'
    
    