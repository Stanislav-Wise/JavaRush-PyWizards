import random
from faker import Faker
from db.session import SessionLocal, engine, Base
from models.genre import Genre
from models.movie import Movie
from models.review import Review


NUM_GENRES = 5
NUM_MOVIES = 10
NUM_MIN_REVIEWS = 5
NUM_MAX_REVIEWS = 5

fake = Faker()
# Faker.seed(123)


def reset_tables(session):
    session.query(Review).delete()
    session.query(Movie).delete()
    session.query(Genre).delete()
    session.commit()


def create_genres(session):
    genres = []

    genres_names_set = set()

    while len(genres_names_set) < NUM_GENRES:
        name = fake.word()
        name = name.capitalize()

        genres_names_set.add(name)

    for name in genres_names_set:
        genre = Genre(name=name)
        session.add(genre)
        genres.append(genre)

    session.commit()
    return genres


def create_movies(session, genres):
    movies = []

    for genre in genres:
        for _ in range(NUM_MOVIES):
            title = fake.sentence(nb_words=3)
            title = title.rstrip('.')
            title = title.capitalize()
            description = fake.paragraph(nb_sentences=3)
            year = random.randint(1950, 2025)

            movie = Movie(
                title=title,
                year=year,
                description=description,
                genre_id=genre.id
            )
            session.add(movie)
            movies.append(movie)

    session.commit()
    return movies


def create_reviews(session, movies):
    reviews_count = random.randint(NUM_MIN_REVIEWS, NUM_MAX_REVIEWS)
    for movie in movies:
        for _ in range(reviews_count):
            rating = random.randint(1, 10)
            text = fake.paragraph(nb_sentences=2)

            review = Review(
                movie_id=movie.id,
                rating=rating,
                text=text,
            )
            session.add(review)
    session.commit()


def main():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as session:
        reset_tables(session)
        genres = create_genres(session)
        print(genres)
        movies = create_movies(session, genres)
        print(movies)
        create_reviews(session, movies)

        print(f'Было создано жанров: {session.query(Genre).count()}')
        print(f'Было создано фильмов: {session.query(Movie).count()}')
        print(f'Было создано отзывов: {session.query(Review).count()}')


if __name__ == '__main__':
    main()