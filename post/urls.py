from django.urls import path
from .views import post_detail,PostList,Home,post_detail,deletepost,Post_Like


from .api import postListApi,postDetailApi,CommentListApi


app_name='post'
urlpatterns = [
    path('',Home,name='home'),
    path('add',PostList,name='post_list'),
    path('<slug:slug>/post_detail',post_detail, name='post_detail'),
    path('<slug:slug>/delete_post',deletepost, name='delete'),
    path('<slug:slug>/like',Post_Like, name='Post_Like'),
    
    
    
    #API
    path('api',postListApi.as_view(),name='post_list'),
    path('<slug:slug>/api_detail',postDetailApi.as_view(),name='postapi_detail'),
    path('api/comment',CommentListApi.as_view()),
]
