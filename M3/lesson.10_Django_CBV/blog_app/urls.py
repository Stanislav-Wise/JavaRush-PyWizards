from django.urls import path
from .views import  about, author_list, author_posts, IndexTemplateView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/add/', PostCreateView.as_view(), name='post_add'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('authors/', author_list, name='author_list'),
    path('authors/<int:author_id>/', author_posts, name='author_posts'),

]