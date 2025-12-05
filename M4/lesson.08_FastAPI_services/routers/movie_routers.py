from fastapi import APIRouter, HTTPException, Query, Depends, status
from schemas.movie import movie_list, MovieBase, MovieCreate, MovieUpdate, MoviePublic, MovieInDBBase

from sqlalchemy.orm import Session
from db.session import get_db


router = APIRouter()


@router.get('/debug-movies')
async def debug_movies(db: Session = Depends(get_db)):
    from models.movie import Movie
    from models.genre import Genre
    from models.review import Review

    movies_count = db.query(Movie).count()
    return {'movies_count': movies_count}


@router.get("/", response_model=list[Movie])
async def movies(
    year: int = Query(None, description="Год выпуска"),
    title: str = Query(None, description="Наименование фильма")
):
    """Вывод фильмов."""
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year >= year]
    if title is not None:
        result = [movie for movie in result if title.lower() in movie.title.lower()]

    return result


@router.get("/{movie_id}/", response_model=Movie)
async def movie_detail(movie_id: int):
    """Вывод одного фильма."""
    length = len(movie_list)
    if movie_id > length or movie_id < 0:
        raise HTTPException(status_code=404, detail='Фильм не найден')

    movie_id -= 1

    movie = movie_list[movie_id]
    return movie


@router.post("/", response_model=MoviePublic, status_code=status.HTTP_201_CREATED)
async def movie_create(movie: MovieCreate):
    """Добавить новый фильм."""
    for m in movie_list:
        if m.title.lower() == movie.title.lower() and m.year == movie.year:
            raise HTTPException(status_code=409, detail='Такой фильм уже есть в базе')
    my_len = len(movie_list) + 1
    new_movie = Movie(
        id=my_len,
        title=movie.title,
        year=movie.year,
        description=movie.description,
    )

    movie_list.append(new_movie)
    return new_movie


@router.put("/{movie_id}/", response_model=Movie)
async def movie_edit(movie_id: int, movie: Movie):
    """Изменить фильм."""

    length = len(movie_list)
    if movie_id > length or movie_id < 0:
        raise HTTPException(status_code=404, detail='Фильм не найден')

    movie_id -= 1

    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year

    return movie


@router.delete("/{movie_id}/")
async def movie_delete(movie_id: int):
    """Удалить фильм."""

    length = len(movie_list)
    if movie_id > length or movie_id < 0:
        raise HTTPException(status_code=404, detail='Фильм не найден')

    movie_id -= 1
    movie = movie_list.pop(movie_id)

    return {'message': f'Фильм {movie.title} {movie.year} был успешно удален'}
