from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import CommentForm,PostForm
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages


def Post_Like(request,slug):
    post=Post.objects.get(slug = slug)
    if request.method=='POST':
        if request.user in post.like.all():
            post.like.remove(request.user)
            is_like=False
        else:
            post.like.add(request.user)
            is_like=True
    post=Post.objects.get(slug = slug)
    html=render_to_string('include/likeform.html',{'post':post})
    return JsonResponse({'result':html})









def Home(request):
    home=Post.objects.all()
    return render(request,'base.html',{'home':home})
    



def PostList(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.save()
            
            
            
                
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})






        
def deletepost(request,slug):
    deleted=Post.objects.get(slug=slug)
    deleted.delete()
    return redirect('/allposts/')




def post_detail(request, slug):
    post=Post.objects.get(slug = slug)
    comment_1 = Comment.objects.all().filter(mypost = post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.mypost = post
            myform.save()
            
            
            comment_1 = Comment.objects.all().filter(mypost = post)
            html=render_to_string('include/comment.html',{'comment_1':comment_1})
            return JsonResponse({'result':html})
            
            

    else:
        form=CommentForm()
    
    return render(request , 'post_detail.html' , {'post':post , 'form':form ,'comment_1':comment_1  })
            
           



    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["comment_1"] = Comment.objects.filter(mypost = self.get_object())
            return context
        
        

        
    
    
        

    














  
# Create your views here.
