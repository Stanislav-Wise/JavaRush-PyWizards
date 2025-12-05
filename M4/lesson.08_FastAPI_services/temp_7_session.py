from db.session import SessionLocal
from models.genre import Genre
from models.movie import Movie
from models.review import Review


session = SessionLocal()

new_genre = Genre(name='Ужасы')

session.add(new_genre)

session.commit()

session.refresh(new_genre)

print(new_genre.name)
print(new_genre.id)

session.close()