from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .models import Post, Author, Comment, Tag
from .forms import PostForm, PostModelForm, PostDeleteForm
from django.contrib import messages


class IndexTemplateView(TemplateView):
    template_name = 'blog_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог JavaRush'
        return context


def about(request):
    return render(request, 'blog_app/about.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'
    # paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.request.GET.get('author')
        min_rating = self.request.GET.get('rating')

        if author_id:
            queryset = queryset.filter(author__id=author_id)
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        # post.views += 1
        post.views = getattr(post, 'views', 0) + 1
        # post.save()
        post.save(update_fields=['views'])
        return super().get(request, *args, **kwargs)


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog_app/post_add.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog_app/post_edit.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')


# def post_delete(request, post_id):
#     """Представление для удаления существующего поста."""
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         form = PostDeleteForm(request.POST)
#         if form.is_valid() and form.cleaned_data['confirm']:
#             post.delete()
#             messages.success(request, f'Пост {post.title} был успешно удален.')
#             return redirect('post_list')
#     else:
#         form = PostDeleteForm()
#     context = {
#         'form': form,
#         'post': post,
#         'title': f'Удалить пост: {post.title}'
#     }
#     return render(request, 'blog_app/post_delete.html', context=context)


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