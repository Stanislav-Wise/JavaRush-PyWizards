import psycopg2
print('psycopg2 установлен')

# POSTGRES_USER: postgres
# POSTGRES_PASSWORD: postgres
# POSTGRES_DB: postgres

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

conn.close()

print('Закрыли подключение к БД')