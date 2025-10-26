from celery import shared_task
import time
from django.core.mail import send_mail
from config import config
from .models import Post


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def send_notification_email(recipient_email, subject, message):
    """Фоновая задача для отправки email."""
    send_mail(
        subject=subject,
        message=message,
        from_email=config.MAIL_HOST_USER, # email отправителя
        recipient_list=[recipient_email],
    )

    return f'Email отправлен {recipient_email}'


@shared_task
def add_views():
    """Периодически увеличивать кол-во просмотров."""
    posts = Post.objects.all()
    for post in posts:
        post.views += 1
        post.save()
    return f'Обновлено {posts.count()} постов'