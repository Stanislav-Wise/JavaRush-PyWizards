from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from schemas.movie import movie_list, Movie


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse, name='movies')
async def movies(
    request: Request,
    year: int = Query(None, description="Год выпуска"),
    title: str = Query(None, description="Наименование фильма")
):
    """Вывод фильмов."""
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year >= year]
    if title is not None:
        result = [movie for movie in result if title.lower() in movie.title.lower()]

    context = {
        "request": request,
        "movies": result,
        "user": 'Guest',
        "title": 'Список фильмов'
    }
    return templates.TemplateResponse("movies/movie_list.html", context=context)


@router.get("/{movie_id}/", response_class=HTMLResponse, name='html_movie_detail')
async def movie_detail(request: Request, movie_id: int):
    """Вывод одного фильма."""
    length = len(movie_list)
    if movie_id > length or movie_id < 0:
        raise HTTPException(status_code=404, detail='Фильм не найден')

    movie_id -= 1

    movie = movie_list[movie_id]
    context = {
        "request": request,
        "movie": movie,
        "user": 'Guest',
        # "title": movie.title
    }
    return templates.TemplateResponse("movies/movie_detail.html", context=context)


