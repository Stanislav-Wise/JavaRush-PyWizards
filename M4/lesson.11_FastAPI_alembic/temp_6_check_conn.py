from db.session import engine


def main():
    print('Проверка начата')

    with engine.connect() as conn:
        print('Соединение установлено')
        result = conn.execute(text('SELECT 111'))

        row = result.fetchone()
        print(f'Результат запроса - {row[0]}')


if __name__ == '__main__':
    from sqlalchemy import text
    main()
