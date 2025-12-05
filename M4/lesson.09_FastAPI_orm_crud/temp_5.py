from db.session import SessionLocal
from models.genre import Genre
from models.movie import Movie
from models.review import Review


session = SessionLocal()

movies = session.query(Movie).all()

for movie in movies:
    print(f'Фильм {movie.title}, год {movie.year}, жанр {movie.genre.name}')


session.close()