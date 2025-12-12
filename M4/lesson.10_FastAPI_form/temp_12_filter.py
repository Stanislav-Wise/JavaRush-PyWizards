from db.session import SessionLocal
from models.genre import Genre
from models.movie import Movie
from models.review import Review


def main():
    session = SessionLocal()

    try:

        print('Фильмы после указанного года')

        query = session.query(Movie)
        query = query.filter(Movie.year > 2015)
        movies = query.all()

        for movie in movies:
            print(f'Фильм: {movie.title}. Год: {movie.year}. Жанр: {movie.genre.name}')

        # movie = session.query(Movie).first()
        # print(f'Фильм: {movie.title}. Год: {movie.year}. Жанр: {movie.genre.name}')


    finally:
        session.close()




if __name__ == '__main__':
    main()