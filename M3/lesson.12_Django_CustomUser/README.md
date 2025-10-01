django-admin --version   
   
# Создать проект   
django-admin startproject blog   
django-admin startproject config .   
   
## Запустить сервер   
python manage.py runserver   

## Создать приложение  
python manage.py startapp blog_app

## Создать миграции
python manage.py makemigrations   
   
## Применить миграции
python manage.py migrate
   
## Интерактивная консоль Django   
python manage.py shell   

## Экспорт данных в фикстуру
python manage.py dumpdata > ./fixtures/blog_app_all_data.json

## Экспорт данных в фикстуру в читаемом виде
python manage.py dumpdata --indent 4 > ./fixtures/blog_app_all_data1.json

## Экспорт данных приложения blog_app в фикстуру в читаемом виде
python manage.py dumpdata blog_app --indent 4 > ./fixtures/blog_app_all_data2.json

## Экспорт данных модели Post из приложения blog_app в фикстуру в читаемом виде
python manage.py dumpdata blog_app.Post --indent 4 > ./fixtures/blog_app_post_data.json

## Импорт данных из фикстуры
python manage.py loaddata ./fixtures/blog_app_all_data2.json   
  
## Создать суперпользователя
python manage.py createsuperuser 

## Тестирование. На реальной БД
pytest --reuse-db