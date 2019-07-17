from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .models import Post, Category
# Create your views here.
def blog(request):
    post = Post.objects.all()
    return render(request, "blog/blog.html",{'posts':post})

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html",{'posts':post})