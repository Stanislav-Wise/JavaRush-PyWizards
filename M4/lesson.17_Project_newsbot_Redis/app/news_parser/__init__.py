from typing import Any, Mapping
import  hashlib
import logging
from datetime import datetime
from app.schemas import NewsItem
from app.news_parser import habr

SOURCE = (
    ('habr', habr.fetch_habr_news_list),
    # ('4pda', pda4.fetch_4pda_news_list)
)

logger = logging.getLogger(__name__)


def generate_news_id(source: str, url: str) -> str:
    """habr:https://habr.com/ru/news/qazxsw123/"""
    base = f'{source}:{url}'
    digest = hashlib.sha256(base.encode("utf-8")).hexdigest()
    return digest


def normalize_published_at(raw_value: Any) -> datetime | None:
    if isinstance(raw_value, datetime):
        return raw_value

    if raw_value is None or raw_value == "":
        return None

    if isinstance(raw_value, str):
        possible_formats = [
            "%Y-%m-%d",
            "%Y-%m-%dT%H:%M",
            "%Y-%m-%dT%H:%M:%S%z",
            "%d.%m-%Y, %H:%M",
        ]

        for possible_format in possible_formats:
            try:
                return datetime.strptime(raw_value, possible_format)
            except ValueError:
                continue
        return None
    return None


def normalize_raw_news(source_name: str, raw_item: Mapping[str, Any]) -> NewsItem:
    raw_title = raw_item.get('title', "")
    title = str(raw_title).strip()

    raw_url = raw_item.get('url') or raw_item.get('link')
    if not raw_url:
        raise ValueError('Не смогли нормализовать url')
    url = str(raw_url).strip()

    raw_summary = raw_item.get("text") or raw_item.get("summary") or ""
    summary = str(raw_summary).strip()

    raw_source = raw_item.get("source") or source_name
    source = str(raw_source).strip()

    raw_published_at = raw_item.get("datetime") or raw_item.get("published_at")
    published_at_dt = normalize_published_at(raw_published_at)

    news_id = generate_news_id(source=source_name, url=url)

    keywords: list[str] = []

    news_item = NewsItem(
        id=news_id,
        title=title,
        url=url,
        summary=summary,
        source=source,
        published_at=published_at_dt,
        keywords=keywords,
    )

    return news_item


def collect_from_all_source() -> list[NewsItem]:
    collected_news: list[NewsItem] = []

    for source_name, fetch_func in SOURCE:
        try:
            raw_items = fetch_func()
        except Exception as exp:
            logger.error(f'Ошибка при парсинге новостей {exp}')
            continue

        # logger.debug(raw_items)

        for raw_item in raw_items:
            try:
                news_item = normalize_raw_news(source_name=source_name, raw_item=raw_item)
            except Exception as exp:
                logger.error(f'Ошибка при нормализации новостей {exp}')
                continue
            collected_news.append(news_item)

    return collected_news


if __name__ == '__main__':
    all_news = collect_from_all_source()
    print(all_news)