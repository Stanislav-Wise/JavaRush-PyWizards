from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .movie_routers import movie_list


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
        "title": movie.title
    }
    return templates.TemplateResponse("movies/movie_detail.html", context=context)

#
# @router.post("/", response_model=Movie, status_code=201)
# async def movie_create(movie: Movie):
#     """Добавить новый фильм."""
#     for m in movie_list:
#         if m.title.lower() == movie.title.lower() and m.year == movie.year:
#             raise HTTPException(status_code=409, detail='Такой фильм уже есть в базе')
#     movie_list.append(movie)
#     return movie
#
#
# @router.put("/{movie_id}/", response_model=Movie)
# async def movie_edit(movie_id: int, movie: Movie):
#     """Изменить фильм."""
#
#     length = len(movie_list)
#     if movie_id > length or movie_id < 0:
#         raise HTTPException(status_code=404, detail='Фильм не найден')
#
#     movie_id -= 1
#
#     movie_list[movie_id].title = movie.title
#     movie_list[movie_id].year = movie.year
#
#     return movie
#
#
# @router.delete("/{movie_id}/")
# async def movie_delete(movie_id: int):
#     """Удалить фильм."""
#
#     length = len(movie_list)
#     if movie_id > length or movie_id < 0:
#         raise HTTPException(status_code=404, detail='Фильм не найден')
#
#     movie_id -= 1
#     movie = movie_list.pop(movie_id)
#
#     return {'message': f'Фильм {movie.title} {movie.year} был успешно удален'}
