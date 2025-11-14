from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    year: int
    description: str


movie_list = [
    Movie(
        title="Mатрица",
        year=1999,
        description="Movie Description 1",
    ),
    Movie(
        title="Звездные войны",
        year=1981,
        description="Movie Description 2",
    ),
    Movie(
        title="Игра",
        year=1999,
        description="Movie Description 3",
    ),
    Movie(
        title="Игра престолов",
        year=2005,
        description="Movie Description 4",
    ),
    Movie(
        title="Терминатор",
        year=1987,
        description="Movie Description 5",
    ),
]

router = APIRouter()


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


@router.post("/", response_model=Movie, status_code=201)
async def movie_create(movie: Movie):
    """Добавить новый фильм."""
    for m in movie_list:
        if m.title.lower() == movie.title.lower() and m.year == movie.year:
            raise HTTPException(status_code=409, detail='Такой фильм уже есть в базе')
    movie_list.append(movie)
    return movie


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
