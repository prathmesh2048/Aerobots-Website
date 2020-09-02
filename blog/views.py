from django.shortcuts import render
from .models import Blog

def blog_list(request):
    blog_list = Blog.objects.all()
    contex = {'blog_list': blog_list,
              }
    return render(request, 'blog/blog_list.html', contex)


def blog_detail(request, slug):
    blog_detail = Blog.objects.get(slug=slug)
    contex = {'blog_detail': blog_detail}
    return render(request, 'blog/blog_detail.html', contex)
