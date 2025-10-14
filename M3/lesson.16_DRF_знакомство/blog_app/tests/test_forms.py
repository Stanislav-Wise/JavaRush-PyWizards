import pytest
from blog_app.models import Author, Post, Tag
from blog_app.forms import PostForm, PostModelForm


@pytest.mark.django_db
def test_post_form_valid():
    form_data = {
        'title': 'Тестовый',
        'content': 'Это содержание поста',
        'rating': 7,
    }
    form = PostForm(data=form_data)

    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['title'] == 'Тестовый'
    assert cleaned_data['content'] == 'Это содержание поста'


@pytest.mark.django_db
def test_post_model_form_valid(author_2):
    tag = Tag.objects.create(name='Python')
    form_data = {
        'author': author_2,
        'title': 'Тестовый Заголовок',
        'content': 'Тестовый Контент',
        'rating': 10,
        'tag': tag,
    }
    form = PostModelForm(data=form_data)

    assert form.is_valid()

    post = form.save()
    assert post.title == form_data.get('title')


@pytest.mark.django_db
def test_post_form_not_valid():
    form_data = {
        'title': 'Тестовый',
        'content': 'Это содержание поста',
        'rating': 117,
    }
    form = PostForm(data=form_data)

    assert not form.is_valid()
