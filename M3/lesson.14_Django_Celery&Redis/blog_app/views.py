from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Post, Author, Comment, Tag
from .forms import PostForm, PostModelForm, PostDeleteForm
from .tasks import send_notification_email


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


class PostDetailView(LoginRequiredMixin, DetailView):
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

        send_notification_email.delay(
            recipient_email='user@mail.ru', # email получчателя
            subject='Новый пост создан',
            message=f'Пост {form.instance.title} был успешно создан'

        )

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


def author_list(request):
    authors = Author.objects.all()
    context = {
        'title': 'Список авторов',
        'authors': authors,
    }
    return render(request, 'blog_app/author_list.html', context=context)


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    context = {
        # 'title': author.name,
        'author': author,
        'posts': posts,
    }
    return render(request, 'blog_app/author_posts.html', context=context)