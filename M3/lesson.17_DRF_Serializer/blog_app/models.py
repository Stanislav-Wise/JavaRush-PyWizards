from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='posts')
    rating = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    image = models.ImageField(upload_to='post_images', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        unique_together = ('title', 'author')


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.author}'


class Author(models.Model):
    name = models.CharField(max_length=100)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author',
        null=True,
        blank=True,
        verbose_name='Пользователь'
    )

    def __str__(self):
        return f'Автор: {self.name}'


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    website = models.URLField(blank=True, null=True)



    def __str__(self):
        return f'Profile of {self.author.name}'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name