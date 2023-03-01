from django.contrib import admin
from .models import Post, Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



    
    
    
admin.site.register(Post)

# Register your models here.
