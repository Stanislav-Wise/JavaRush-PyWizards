from db.session import SessionLocal
from models.genre import Genre
from models.movie import Movie
from models.review import Review


session = SessionLocal()

# genre = session.query(Genre).first()
genre = session.query(Genre).filter_by(name='Боевик').first()

print(genre)
print(genre.name)
print(genre.id)

if genre is not None:
    new_movie = Movie(
        title='Игра Престолов',
        year=2015,
        description='Фэнтези про браконов',
        # genre=genre  #
        genre_id = genre.id

    )

    session.add(new_movie)
    session.commit()
    print(new_movie)
    print(new_movie.id)
    print(new_movie.title)

else:
    print('Жанр не найден')

session.close()