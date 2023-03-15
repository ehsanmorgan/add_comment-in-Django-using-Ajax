from rest_framework import serializers
from .models import Post,Comment

class postSerializer(serializers.ModelSerializer):
    like=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model=Comment
        fields=['name','body','created_on']
        
        

class postDetailSerializer(serializers.ModelSerializer):
    like=serializers.StringRelatedField()
    mypost=CommentSerializer(source='comments',many=True)
    class Meta:
        model=Post
        fields='__all__'
        
        
        
