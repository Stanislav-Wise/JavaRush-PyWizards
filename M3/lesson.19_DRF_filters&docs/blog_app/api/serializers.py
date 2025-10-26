from rest_framework import serializers
from blog_app.models import Author, Tag, Comment, Post


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для поста."""

    # Только на запись
    # author = serializers.PrimaryKeyRelatedField(
    #     queryset=Author.objects.all(),
    #     write_only=True,
    #     help_text='ID автора.'
    # )
    # tags = serializers.PrimaryKeyRelatedField(
    #     queryset=Tag.objects.all(),
    #     write_only=True,
    #     help_text='Список ID тэгов.'
    # )
    # # Только на чтение
    # author_name = serializers.CharField(
    #     source='author.name',
    #     read_only=True,
    # )
    # author_email = serializers.SerializerMethodField(read_only=True)
    # tags_info = serializers.SerializerMethodField(read_only=True)
    #
    # def get_author_email(self, obj):
    #     """Вернём email пользователя."""
    #     user = getattr(obj.author, 'user', None)
    #     return getattr(user, 'email', None)
    #
    # def get_tags_info(self, obj):
    #     """Вернём список с тэгами."""
    #     return [{"id": tag.id, "name": tag.name} for tag in obj.tags.all() ]

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            # Запись
            'author',
            'tags',
            # Чтение
            # 'author_name',
            # 'author_email',
            # 'tags_info',
            'created_at',
            'rating',
            'views',
        )
        read_only_fields = ('created_at',)


class AuthorSerializer(serializers.ModelSerializer):
    # Для чтения
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'user_id', 'user_email')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CommentSerializer(serializers.ModelSerializer):
    # Только на запись
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        write_only=True,
        help_text='ID автора.'
    )
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        write_only=True,
        help_text='ID поста.'
    )
    # Только на чтение
    author_name = serializers.CharField(
        source='author.name',
        read_only=True,
    )
    author_email = serializers.SerializerMethodField(read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    def get_author_email(self, obj):
        """Вернём email пользователя."""
        user = getattr(obj.author, 'user', None)
        return getattr(user, 'email', None)

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            # Запись
            'author',
            'post',
            # Чтение
            'author_name',
            'author_email',
            'post_title',
            'created_at',
        )
        read_only_fields = ('created_at',)