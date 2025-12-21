from fastapi import APIRouter, status
from app.schemas import NewsItem, fake_news_list, PublishedNews, Keyword


router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.get("/news/", response_model=list[NewsItem],status_code=status.HTTP_200_OK)
async def news_list() -> list[NewsItem]:
    return fake_news_list