# Запуск сервера  
uvicorn main:app --reload  

#
pip install fastapi[all]
  
# alembic
## Посмотреть версию
alembic --version

## Инициализировать alembic в проекте в диреторию alembic
alembic init alembic

## Текущая версия
alembic current

## Создаем первую ревизию\миграцию с сообщением "init"
alembic revision --autogenerate -m "init"

## История миграций
alembic history

## Расширенная история миграций
alembic history --verbose

## Применить последнюю миграцию 
alembic upgrade head

## Применить миграцию 1b96ca033418
alembic upgrade 1b96ca033418

## Откатиться на 1 шаг назад
alembic downgrade -1

## Откатиться к миграции ef50581b07eb
alembic downgrade ef50581b07eb

## Откатиться к базовому состоянию
alembic downgrade base