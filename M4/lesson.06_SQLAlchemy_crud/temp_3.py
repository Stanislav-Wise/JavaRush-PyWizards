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

# session.commit()

session.close()