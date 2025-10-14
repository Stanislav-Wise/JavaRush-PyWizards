from rest_framework import serializers
from blog_app.models import Author, Tag, Comment, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
