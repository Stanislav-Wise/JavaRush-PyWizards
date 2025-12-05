from fastapi import APIRouter, HTTPException, Query, Depends, status
from schemas.movie import movie_list, MovieBase, MovieCreate, MovieUpdate, MoviePublic, MovieInDBBase
from models.movie import Movie
from models.genre import Genre
from models.review import Review
from sqlalchemy.orm import Session
from db.session import get_db
from services.movie_service import list_movie, get_movie_by_id, create_movie


router = APIRouter(
    tags=["api movies"],
    prefix="/api/v2/movies",
)


@router.get('/debug-movies')
async def debug_movies(db: Session = Depends(get_db)):
    movies_count = db.query(Movie).count()
    return {'movies_count': movies_count}


@router.get("/", response_model=list[MoviePublic])
async def movies(
    db: Session = Depends(get_db),
    year: int = Query(None, description="Год выпуска"),
    # title: str = Query(None, description="Наименование фильма"),
    genre: str = Query(None, description="Наименование ;fyhf")
):
    """Вывод фильмов."""
    # query = db.query(Movie)
    # if year is not None:
    #     query = query.filter(Movie.year >= year)
    # if title is not None:
    #     query = query.filter(Movie.title.ilike(f"%{title}%"))
    #
    # query = query.order_by(Movie.year.desc(), Movie.title.asc())
    #
    # movie_db = query.all()

    movie_db = list_movie(
        session=db,
        year_from=year,
        genre_name=genre
    )

    return movie_db


@router.get("/{movie_id}/", response_model=MoviePublic)
async def movie_detail(
    movie_id: int,
    db: Session = Depends(get_db),
):
    """Вывод одного фильма."""
    movie = get_movie_by_id(db, movie_id)

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Фильм c id {movie_id} не найден')

    return movie


@router.post("/", response_model=MoviePublic, status_code=status.HTTP_201_CREATED)
async def movie_create(
    movie_in: MovieCreate,
    db: Session = Depends(get_db),
):
    """Добавить новый фильм."""

    if movie_in.genre_id is not None:
        genre = db.query(Genre).filter(Genre.id == movie_in.genre_id).first()

        if genre is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Жанр c id {movie_in.genre_id} не найден')

    # new_movie = Movie(
    #     title=movie_in.title,
    #     year=movie_in.year,
    #     description=movie_in.description,
    #     genre_id=movie_in.genre_id,
    # )
    #
    # db.add(new_movie)
    # db.commit()
    # db.refresh(new_movie)
    #
    new_movie = create_movie(
        session=db,
        title=movie_in.title,
        year=movie_in.year,
        description=movie_in.description,
        genre_name=genre.name
    )

    return new_movie


@router.put("/{movie_id}/", response_model=MoviePublic)
async def movie_edit(
    movie_id: int,
    movie_in: MovieUpdate,
    db: Session = Depends(get_db),
):
    """Изменить фильм."""

    movie = get_movie_by_id(db, movie_id)

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Фильм c id {movie_id} не найден')

    movie.title = movie_in.title
    movie.year = movie_in.year
    movie.description = movie_in.description
    movie.genre_id = movie_in.genre_id

    db.commit()
    db.refresh(movie)

    return movie




@router.delete("/{movie_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def movie_delete(
    movie_id: int,
    db: Session = Depends(get_db),
):
    """Удалить фильм."""

    movie = get_movie_by_id(db, movie_id)

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Фильм c id {movie_id} не найден')

    db.delete(movie)
    db.commit()

    return None
