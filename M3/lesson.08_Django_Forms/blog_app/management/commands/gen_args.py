from django.core.management.base import BaseCommand
from blog_app.models import Post, Author, Comment
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Генерация тестовых данных для моделей Author, Post, Comment'

    def add_arguments(self, parser):
        """Добавляет аргумент для команды."""
        parser.add_argument('--num', type=int, default=5, help='Кол-во')

    def handle(self, *args, **kwargs):
        self.stdout.write('Начинаем генерацию тестовых данных...')

        num = kwargs['num']

        fake = Faker()

        authors = []
        for _ in range(num):
            author_name = fake.name()
            author = Author.objects.create(name=author_name)
            authors.append(author)
        self.stdout.write(f'Создано {len(authors)} авторов.')

        posts = []
        for _ in range(num):
            post_title = fake.sentence(nb_words=random.randint(3, 10))
            post_content = fake.text(max_nb_chars=200)
            post_author = random.choice(authors)
            post = Post.objects.create(
                title=post_title,
                content=post_content,
                author=post_author,
                rating=random.randint(0, 10)
            )
            posts.append(post)
        self.stdout.write(f'Создано {len(posts)} постов.')

        comments = []
        for _ in range(num):
            comment_text = fake.text(max_nb_chars=100)
            comment_post = random.choice(posts)
            comment_author = random.choice(authors)
            comment = Comment.objects.create(
                text=comment_text,
                post=comment_post,
                author=comment_author,
            )
            comments.append(comment)
        self.stdout.write(f'Создано {len(comments)} комментариев.')

        self.stdout.write('Генерация тестовых данных завершена')