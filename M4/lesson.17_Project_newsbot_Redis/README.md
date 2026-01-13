python -m venv .venv

# Создать и запустить докер контейнер Redis
docker run --name pw-newsbot-redis -p 6379:6379 -d redis:7-alpine

# Установить библиотеку redis
pip install "redis>=7.0, <8"
poetry add redis

# Установить библиотеку celery
pip install "celery>=5.0, <6"
poetry add celery

# Запустить celery
celery -A celery_worker.celery_app worker -l INFO