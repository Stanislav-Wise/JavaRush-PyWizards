import psycopg2
from pprint import pprint


print('psycopg2 установлен')

db = 'dvd'
user = 'postgres'
password = 'postgres'
host = 'localhost1'
port = ('5432')


try:
    with psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port) as connection:

        print('Успешное подключение к БД')

        name = "Nancy"

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM customer_copy1 WHERE first_name = %s;", (name, ))


            rows = cursor.fetchall()

            print(rows)
            print(type(rows))
            print(len(rows))
except Exception as e:
    print(f'Ошибка {e}')





print('Закрыли подключение к БД')