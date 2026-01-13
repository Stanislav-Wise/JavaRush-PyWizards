from fastapi import APIRouter, status
from app.schemas import NewsItem, fake_news_list, PublishedNews, Keyword
from app.news_parser import collect_from_all_source
from app.redis_client import ping_redis
from app.tasks import ping


router = APIRouter()


@router.get("/health/")
async def health_check():
    redis_ok = ping_redis()
    celery_ping = ping.delay()
    return {
        "FastAPI": "ok",
        "redis": redis_ok,
        'celery': celery_ping.get(timeout=10),
    }


@router.get("/news/", response_model=list[NewsItem],status_code=status.HTTP_200_OK)
async def news_list() -> list[NewsItem]:
    return fake_news_list


@router.get("/news/scrape/", response_model=list[NewsItem],status_code=status.HTTP_200_OK)
async def scrape_news():
    news_items = collect_from_all_source()
    return news_items