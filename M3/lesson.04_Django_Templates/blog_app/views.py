from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'blog_app/index.html')


def about(request):
    return render(request, 'blog_app/about.html')


def post_list(request):
    posts = Post.objects.all()
    context = {
        'title': 'Список постов',
        'posts': posts,
    }
    return render(request, 'blog_app/post_list.html', context=context)