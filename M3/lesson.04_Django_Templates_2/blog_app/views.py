from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Comment, Tag


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


def post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    tags = post.tags.all()

    context = {
        # 'title': post.title,
        'post': post,
        'comments': comments,
        'tags': tags,

    }
    return render(request, 'blog_app/post_detail.html', context=context)


def author_list(request):
    authors = Author.objects.all()
    context = {
        'title': 'Список авторов',
        'authors': authors,
    }
    return render(request, 'blog_app/author_list.html', context=context)


def author_posts(request, author_id):
    # post = Post.objects.get(id=post_id)
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    context = {
        # 'title': author.name,
        'author': author,
        'posts': posts,
    }
    return render(request, 'blog_app/author_posts.html', context=context)