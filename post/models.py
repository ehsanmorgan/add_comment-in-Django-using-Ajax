from django.db import models
from django .utils.text import slugify
from django.contrib.auth.models import User








class Post(models.Model):
    
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=100000)
    image=models.ImageField(null=True,blank=True)
    tags=models.CharField(max_length=10)
    craete_date=models.DateTimeField
 

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
       self.slug=slugify(self.title)
       super(Post, self).save(*args, **kwargs)
       
       
     
    
   
    
    

   






class Comment(models.Model):
    mypost = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name

# Create your models here.
