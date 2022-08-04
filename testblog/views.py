from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
    
    me = User.objects.get(username='cuff')

    Post.objects.create(author=me, title="First_title", text="I adore wordplay", created_date=timezone.now()) 
    Post.objects.create(author=me, title="Second_title", text="I could adore wordplay", created_date=timezone.now()) 
    Post.objects.create(author=me, title="Third_title", text="I would adore wordplay", created_date=timezone.now()) 
    Post.objects.create(author=me, title="Fourth_title", text="I play with wordplay", created_date=timezone.now()) 
    Post.objects.create(author=me, title="Fifth_title", text="I may adore wordplay", created_date=timezone.now()) 

    post = Post.objects.all()
    for p in post:
        p.publish()
    return render(request, "blog/post_list.html", {'posts':post})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    return render(request, 'post_details.html', {'post':post})