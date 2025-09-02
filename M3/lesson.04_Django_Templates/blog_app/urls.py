from django.urls import path
from .views import index, about, post_list


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('posts/', post_list, name='post_list'),

]