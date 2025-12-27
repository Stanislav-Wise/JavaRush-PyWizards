from typing import Any, Mapping
import  hashlib
from datetime import datetime
from app.schemas import NewsItem


def generate_news_id(sourse: str, url: str) -> str:
    """habr:https://habr.com/ru/news/qazxsw123/"""
    base = f'{sourse}:{url}'
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


def normalize_raw_news(source_name, raw_item) -> NewsItem:
    raw_title = raw_item.get('title', "")
    title = str(raw_title).strip()

    raw_url = raw_item.get('url') or raw_item.get('link')
    if not raw_url:
        raise ValueError('Не смогли нормализовать url')
    url = str(raw_url).strip()

