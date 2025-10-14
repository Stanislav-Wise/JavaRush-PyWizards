import pytest
from django.urls import reverse
from bs4 import BeautifulSoup

from blog_app.models import Post, Author


@pytest.mark.django_db
def test_post_list_template(client, author_1, author_2, post_1, post_2, post_3):
    url = reverse('post_list')
    response = client.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')
    titles = [h4.get_text(strip=True) for h4 in soup.find_all('h4')]
    assert 'Тестовый пост 1' in titles
    assert 'Тестовый пост 2' in titles
    assert 'Тестовый пост 3' in titles

    # assert soup.find('title', text='')