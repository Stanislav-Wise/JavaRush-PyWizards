from db.session import Base, engine
import models.genre
import models.movie
import models.review


if __name__ == '__main__':
    print('Создаём таблицы...')
    Base.metadata.create_all(bind=engine)
    print('Все таблицы созданы.')

    # CREATE TABLE IF NOT EXISTS movies (
    #     id
    #     title