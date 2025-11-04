from fastapi import FastAPI, HTTPException
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
app = FastAPI()

@app.get("/")
@app.get("/home/")
async def index():
    """Главная страница."""
    return {"message": "Hello World!!!"}


@app.get("/about/")
async def about():
    """Страница о нас."""
    return {"message": "Страница о нас."}


@app.get("/movies/", response_model=list[Movie])
async def movies():
    """Вывод фильмов."""
    # print(movie_list)
    return movie_list


@app.get("/movies/{movie_id}/", response_model=Movie)
async def movie_detail(movie_id: int):
    """Вывод одного фильма."""
    length = len(movie_list)
    if movie_id > length or movie_id < 0:
        raise HTTPException(status_code=404, detail='Фильм не найден')

    movie_id -= 1

    movie = movie_list[movie_id]
    # print(movie)
    return movie


@app.post("/movies/", response_model=Movie, status_code=201)
async def movie_create(movie: Movie):
    """Добавить новый фильм."""
    movie_list.append(movie)
    return movie