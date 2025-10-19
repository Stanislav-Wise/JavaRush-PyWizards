from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError

from blog_app.api.permissions import IsOwnerOrReadOnly
from blog_app.api.serializers import PostSerializer, CommentSerializer, AuthorSerializer, TagSerializer
from blog_app.models import Post, Comment, Author, Tag


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # def get_permissions(self):

    def get_queryset(self):
        qs = super().get_queryset()

        return qs

    def perform_create(self, serializer):
        user = self.request.user
        author = getattr(user, 'author', None)

        if author is None:
            raise ValidationError('Нет привязанного автора')

        serializer.save(author=author)

    def perform_update(self, serializer):
        instance = self.get_object()
        serializer.save(author=instance.author)