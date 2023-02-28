from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    
    
    
admin.site.register(Post,SomeModelAdmin)

# Register your models here.
