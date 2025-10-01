import pytest
from django.urls import reverse


def test_index_views(client):
    """Тест для проверки главной страницы."""
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

    assert 'Блог JavaRush' in response.content.decode('utf-8')



@pytest.mark.django_db
def test_post_list_view(client, author_1, author_2, post_1, post_2, post_3):
    """Тест для проверки cстраницы списка постов."""
    url = reverse('post_list')
    response = client.get(url)
    assert response.status_code == 200

    assert post_1.title.encode() in response.content
