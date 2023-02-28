from django.db import models
from django .utils.text import slugify






class Post(models.Model):
    
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=100000)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       self.slug=slugify(self.title)
       super(Post, self).save(*args, **kwargs)
       
       
     
    
   
    
    

   






class Comment(models.Model):
    mypost = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name

# Create your models here.
