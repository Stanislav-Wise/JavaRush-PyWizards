from fastapi import APIRouter, status
from app.schemas import NewsItem, fake_news_list, PublishedNews, Keyword
from app.news_parser import collect_from_all_source


router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.get("/news/", response_model=list[NewsItem],status_code=status.HTTP_200_OK)
async def news_list() -> list[NewsItem]:
    return fake_news_list


@router.get("/news/scrape/", response_model=list[NewsItem],status_code=status.HTTP_200_OK)
async def scrape_news():
    news_items = collect_from_all_source()
    return news_items