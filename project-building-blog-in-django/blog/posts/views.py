from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts': posts})

def post(request):
    posts = Post.object.get(id=pk)
    return render(request, 'posts.html')
