import pytest
from blog_app.models import Author, Post


@pytest.mark.django_db
def test_author_creation(author_1, author_2):
    assert Author.objects.count() == 2
    assert author_1.name == 'Боб'
    assert str(author_1) == 'Автор: Боб'


@pytest.mark.django_db
def test_post_creation(post_1, post_2, post_3, author_2):
    assert Post.objects.count() == 3
    assert post_3.title == "Тестовый пост 3"
    assert Post.objects.filter(author=author_2).count() == 2