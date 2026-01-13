import time
import logging
from celery import Celery
from app.config import settings
from app.news_parser import collect_from_all_source


logger = logging.getLogger(__name__)

celery_app = Celery(
    "newsbot",
    broker=settings.redis_url,
    backend=settings.redis_url,
)


celery_app.conf.update(
    timezone="UTC",
    enable_utc=True,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    broker_connection_retry_on_startup=True,
    result_expires=3600,
    task_default_queue="newsbot",
)

@celery_app.task(name="app.tasks.ping")
def ping():
    return True


@celery_app.task(name="app.tasks.collect_news")
def collect_news() -> list[dict]:
    pass