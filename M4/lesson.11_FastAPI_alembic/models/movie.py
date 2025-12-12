from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(Text)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    duration = Column(Integer, nullable=True)

    # movie.genre.name
    genre = relationship("Genre", back_populates="movies")
    reviews = relationship("Review", back_populates="movie")