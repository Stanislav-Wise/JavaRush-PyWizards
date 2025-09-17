from django.urls import path
from .views import index, about, post_list, author_list, post_detail, author_posts, post_add


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('posts/', post_list, name='post_list'),
    path('posts/add/', post_add, name='post_add'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('authors/', author_list, name='author_list'),
    path('authors/<int:author_id>/', author_posts, name='author_posts'),

]