from pydantic import BaseModel, Field, AnyHttpUrl
from datetime import datetime
from uuid import UUID


class NewsItem(BaseModel):
    id: str = Field(
        ...,
        description="ID news item.",
        examples=['fhyy5fhg443asdgfhqwe']
    )
    title: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="Title of the news item.",
        examples=['Django 6.0 released', 'Вышла новая версия Python 3.14']
    )
    # url: AnyHttpUrl = Field(
    url: str = Field(
        ...,
        description="URL original arcticle.",
        examples=['http://habr.com/news/python/1234']
    )
    summary: str = Field(
        default=None,
        description="Summary of the news item.",
        examples=['Краткий обзор Django 6.0 и его ключевые отличия']
    )
    source: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Source of the news item.",
        examples=['habr', 'rbc']
    )
    published_at: datetime | None = Field(
        ...,
        description="Original date published the news.",
        examples=['2025-12-16T20:30:00Z']
    )
    keywords: list[str] = Field(
        default_factory=list,
        description="Keywords of the news item.",
        examples=[["python", "django", "fastapi"]]
    )


class PublishedNews(BaseModel):
    news_id: str = Field(
        ...,
        description="ID of news item.",
        examples=['fhyy5fhg443asdgfhqwe']
    )
    published_at: datetime = Field(
        ...,
        description="Date published the news ti the Telegram channelk",
        examples=['2025-12-16T20:30:00Z']
    )
    channel_id: str = Field(
        ...,
        description="Channel id of the news item.",
        examples=["@my_channel", "-100101234567"]
    )


class Keyword(BaseModel):
    id: int = Field(
        ...,
        description='Keyword id.',
        examples=[1, 2, 3]
    )
    word: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Keyword word.",
        examples=['python', 'django']
    )


fake_news_list = [
    NewsItem(
        id='fhyy5fhg443asdgfhqwe',
        title='Django 6.0 released',
        url='http://habr.com/news/python/1234',
        summary='Django 6.0 released summary',
        source='habr',
        published_at="2025-12-16T20:30:00Z",
        keywords=['python', 'django']
    ),
    NewsItem(
        id='fhyy5fhg443asdgfhqwe',
        title='Django 6.0 released',
        url='http://habr.com/news/python/1234',
        summary='Django 6.0 released summary',
        source='habr',
        published_at="2025-12-16T20:30:00Z",
        keywords=['python', 'django']
    ),
    NewsItem(
        id='fhyy5fhg443asdgfhqwe222',
        title='Django 7.0 released',
        url='http://habr.com/news/python/2345',
        summary='Django 7.0 released summary',
        source='rbc',
        published_at="2025-12-16T20:40:00Z",
        keywords=['fastapi', 'django']
    ),
    NewsItem(
        id='fhyy5fhg443asdgfhqwe333',
        title='Django 8.0 released',
        url='http://habr.com/news/python/345678',
        summary='Django 8.0 released summary',
        source='habr',
        published_at="2025-12-16T20:50:00Z",
        keywords=['python', 'fastapi']
    ),
]