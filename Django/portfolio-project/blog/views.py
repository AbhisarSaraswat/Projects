from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def details(request,blogid):
    blog = get_object_or_404(Blog,pk=blogid)
    return render(request, 'blog/detail.html',{'blog':blog})