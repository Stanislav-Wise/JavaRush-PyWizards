import psycopg2
from pprint import pprint


print('psycopg2 установлен')

db = 'dvd'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'


conn = psycopg2.connect(
    dbname=db,
    user=user,
    password=password,
    host=host,
    port=port
)

print('Успешное подключение к БД')

name = "Nancy' OR 1=1 --"
cursor = conn.cursor()
cursor.execute("SELECT * FROM customer_copy1 WHERE first_name = %s;", (name, ))


rows = cursor.fetchall()

print(rows)
print(type(rows))
print(len(rows))


cursor.close()
conn.close()

print('Закрыли подключение к БД')