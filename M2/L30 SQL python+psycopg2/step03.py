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

cursor = conn.cursor()
cursor.execute('SELECT * FROM customer;')

rows = cursor.fetchone()

print(rows)
print(type(rows))


rows = cursor.fetchone()

print(rows)
print(type(rows))


rows = cursor.fetchone()

print(rows)
print(type(rows))


cursor.close()
conn.close()

print('Закрыли подключение к БД')