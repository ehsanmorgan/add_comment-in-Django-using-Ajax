from rest_framework import serializers
from .models import Post

class postSerializer(serializers.ModelSerializer):
    like=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'
        
        
        

class postDetailSerializer(serializers.ModelSerializer):
    like=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'