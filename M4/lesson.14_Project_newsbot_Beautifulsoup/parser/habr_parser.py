from bs4 import BeautifulSoup
from pathlib import Path
import requests


def parser_habr_list_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, 'html.parser')
    news_items: list[dict] = []

    article_tags = soup.select('article.tm-articles-list__item')

    for article_tag in article_tags:

        title_link = article_tag.find("a", class_="tm-title__link")

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


if __name__ == '__main__':
    response = requests.get('https://habr.com/ru/news/', timeout=10)
    response.raise_for_status()
    html_text = response.text

    # html_path = Path('./data/habr_news.html')
    # html_text = html_path.read_text(encoding='utf-8')

    news = parser_habr_list_html(html_text)
    for news_item in news:
        print(f"""{news_item.get('title')}
{news_item.get('url')}
{news_item.get('datetime')}
{news_item.get('text')}
{news_item.get('source')}
""")
