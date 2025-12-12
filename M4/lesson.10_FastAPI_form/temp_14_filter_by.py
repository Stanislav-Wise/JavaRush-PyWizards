from db.session import SessionLocal
from models.genre import Genre
from models.movie import Movie
from models.review import Review


def main():
    session = SessionLocal()

    try:


        movies = session.query(Movie).filter((Movie.year > 2015) & (Movie.genre_id==1)).all()
        # movie = session.query(Movie).filter_by(year=2015).first()

        # movies = genre.movies
        #
        for movie in movies:
            print(f'Фильм: {movie.title}. Год: {movie.year}. Жанр: {movie.genre.name}')

        # movie = session.query(Movie).first()
        # print(f'Фильм: {movie.title}. Год: {movie.year}. Жанр: {movie.genre.name}')


    finally:
        session.close()




if __name__ == '__main__':
    main()