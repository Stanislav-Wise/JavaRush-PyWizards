from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend

from blog_app.api.paginations import PostSmallPagination
from blog_app.api.permissions import IsOwnerOrReadOnly
from blog_app.api.serializers import PostSerializer, CommentSerializer, AuthorSerializer, TagSerializer
from blog_app.models import Post, Comment, Author, Tag


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PostSmallPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('author', 'tags', 'rating')

    # def get_permissions(self):

    def get_queryset(self):
        qs = super().get_queryset()

        # params = self.request.query_params
        #
        # author_id = params.get('author')
        # if author_id:
        #     try:
        #         author_int_id = int(author_id)
        #     except ValueError:
        #         author_int_id = None
        #     if author_int_id is not None:
        #         qs = qs.filter(author=author_int_id)
        #
        # rating = params.get('rating')
        # if rating:
        #     try:
        #         rating_int = int(rating)
        #     except ValueError:
        #         rating_int = None
        #     if rating is not None:
        #         qs = qs.filter(rating=rating_int)
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


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
