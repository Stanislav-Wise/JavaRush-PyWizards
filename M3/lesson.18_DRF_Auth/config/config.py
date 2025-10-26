from dotenv import load_dotenv
import os


load_dotenv()

MY_SECRET_KEY = os.getenv("SECRET_KEY")

MY_CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")

MAIL_HOST = os.getenv("EMAIL_HOST")
MAIL_PORT = os.getenv("EMAIL_PORT")
MAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
MAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
MAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")