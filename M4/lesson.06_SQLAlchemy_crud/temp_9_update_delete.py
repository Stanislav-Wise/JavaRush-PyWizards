from db.session import SessionLocal
from models.genre import Genre
from models.movie import Movie
from models.review import Review


session = SessionLocal()


# # UPDATE
#
# genre = session.query(Genre).first()
# print(f' - {genre.name} - {genre.id}')
#
# genre.name = 'Детектив'
#
# session.commit()
#
# session.refresh(genre)
# genre = session.query(Genre).first()
# print(f' - {genre.name} - {genre.id}')


# DELETE

genre = session.query(Genre).filter_by(name='Боевик').first()
print(f' - {genre.name} - {genre.id}')

session.delete(genre)

session.commit()

session.refresh(genre)

genre = session.query(Genre).filter_by(name='Боевик')
print(f' - {genre}')


session.close()

