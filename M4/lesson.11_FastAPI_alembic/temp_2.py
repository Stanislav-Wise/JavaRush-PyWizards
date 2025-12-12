from db.session import SessionLocal
from models.genre import Genre
from models.movie import Movie
from models.review import Review


session = SessionLocal()

# new_genre = Genre(name='Комедия')
# session.add(new_genre)

new_genre1 = Genre(name='Боевик')
new_genre2 = Genre(name='Фантасика')

session.add_all([new_genre1, new_genre2])
session.commit()

session.close()