from django.urls import path
from .views import post_detail,PostList,Home,post_detail,deletepost


app_name='post'
urlpatterns = [
    path('',Home,name='home'),
    path('add',PostList,name='post_list'),
    path('<slug:slug>/post_detail',post_detail, name='post_detail'),
    path('<slug:slug>/delete_post',deletepost, name='delete'),
    
]
