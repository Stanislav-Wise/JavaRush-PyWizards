import requests
# from requests import RequestException
from bs4 import BeautifulSoup
from pathlib import Path
from typing import Any
import logging


HABR_BASE_URL = 'https://habr.com/ru'
HABR_NEWS_URL = f'{HABR_BASE_URL}/news/'
HABR_ARTICLE_URL = f'{HABR_BASE_URL}/article/'

HABR_CARD_SELECTOR = 'article.tm-articles-list__item'
HABR_TITLE_SELECTOR = 'a'
HABR_TITLE_LINK_SELECTOR = 'tm-title__link'

DEFAULT_HEADERS = {
    'User-Agent': "Mozilla/5.0",
    'Accept': 'text/html',
}


logger = logging.getLogger(__name__)


def parser_habr_list_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, 'html.parser')
    news_items: list[dict] = []

    article_tags = soup.select(HABR_CARD_SELECTOR)

    for article_tag in article_tags:

        title_link = article_tag.find(HABR_TITLE_SELECTOR, class_=HABR_TITLE_LINK_SELECTOR)

        if title_link is None:
            continue

        title_text = title_link.get_text(strip=True)
        relative_url = title_link.get('href', '')

        if relative_url is None:
            continue

        if relative_url.startswith('http'):
            full_url = relative_url
        else:
            full_url = f'https://habr.com{relative_url}'

        news_date_row = article_tag.find("time")
        news_date = news_date_row.get('datetime', '')

        text_row = article_tag.find("p")
        text = text_row.get_text(strip=True)

        news_item = {
            'title': title_text,
            'url': full_url,
            'source': 'habr',
            'datetime': news_date,
            'text': text,
        }

        news_items.append(news_item)

    return news_items


def fetch_habr_news_list(limit: int = 20) -> list[dict[str, str]]:
    raw_items: list[dict[str, str]] = []

    try:
        response = requests.get(HABR_NEWS_URL, headers=DEFAULT_HEADERS, timeout=10)
    except requests.RequestException as exc:
        logger.warning(f'При парсинге возникла ошибка {exc}')
        return raw_items

    if response.status_code != 200:
        logger.warning(f'При парсинге возник статус код {response.status_code}')
        return raw_items

    raw_items = parser_habr_list_html(response.text)
    return raw_items




if __name__ == '__main__':
    # response = requests.get(HABR_NEWS_URL, headers=DEFAULT_HEADERS, timeout=10)
    # response.raise_for_status()
    # html_text = response.text

    # html_path = Path('./data/habr_news.html')
    # html_text = html_path.read_text(encoding='utf-8')

    # news = parser_habr_list_html(html_text)

    news = fetch_habr_news_list()

    for news_item in news:
        print(f"""{news_item.get('title')}
{news_item.get('url')}
{news_item.get('datetime')}
{news_item.get('text')}
{news_item.get('source')}
""")
