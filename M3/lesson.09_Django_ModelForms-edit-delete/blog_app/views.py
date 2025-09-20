from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Comment, Tag
from .forms import PostForm, PostModelForm, PostDeleteForm
from django.contrib import messages


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


# def post_add(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data['title'],
#                 content=form.cleaned_data['content'],
#                 rating=form.cleaned_data['rating'],
#                 author=Author.objects.first(),
#             )
#             return redirect('post_list')
#     else:
#         form = PostForm()
#
#     context = {
#         'form': form,
#         'title': 'Добавить пост'
#     }
#     return render(request, 'blog_app/post_add.html', context=context)


def post_add(request):
    """Представление для создания нового поста."""

    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Пост был успешно добавлен.')
            return redirect('post_list')
    else:
        form = PostModelForm()

    context = {
        'form': form,
        'title': 'Добавить пост'
    }
    return render(request, 'blog_app/post_add.html', context=context)


def post_edit(request, post_id):
    """Представление для редактирования существующего поста."""
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'Пост {post.title} был успешно обновлен.')
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)

    context = {
        'form': form,
        'title': f'Редактировать пост: {post.title}'
    }
    return render(request, 'blog_app/post_edit.html', context=context)


def post_delete(request, post_id):
    """Представление для удаления существующего поста."""
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            post.delete()
            messages.success(request, f'Пост {post.title} был успешно удален.')
            return redirect('post_list')
    else:
        form = PostDeleteForm()
    context = {
        'form': form,
        'post': post,
        'title': f'Удалить пост: {post.title}'
    }
    return render(request, 'blog_app/post_delete.html', context=context)


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