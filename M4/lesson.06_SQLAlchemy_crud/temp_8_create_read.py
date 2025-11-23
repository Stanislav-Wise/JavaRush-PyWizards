from db.session import SessionLocal
from models.genre import Genre
from models.movie import Movie
from models.review import Review


session = SessionLocal()

# CREATE
# new_genre = Genre(name='Комедия')
# session.add(new_genre)

# new_genre1 = Genre(name='Боевик')
# new_genre2 = Genre(name='Фантасика')
#
# session.add_all([new_genre1, new_genre2])
# session.commit()


# READ
# .all()
# genres = session.query(Genre).all()  # SELECT * FROM genres;
#
# for genre in genres:
#     print(f' - {genre.name} - {genre.id}')


# .first()
# genre = session.query(Genre).first()
# print(f' - {genre.name} - {genre.id}')


# filter_by()
genre = session.query(Genre).filter_by(name='Боевик').first() # WHERE name = 'Боевик'
print(f' - {genre.name} - {genre.id}')

session.close()

