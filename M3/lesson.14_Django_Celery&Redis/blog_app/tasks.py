from celery import shared_task
import time
from django.core.mail import send_mail


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
        from_email='admin@post.ru', # email отправителя
        recipient_list=[recipient_email],
    )

    return f'Email отправлен {recipient_email}'
