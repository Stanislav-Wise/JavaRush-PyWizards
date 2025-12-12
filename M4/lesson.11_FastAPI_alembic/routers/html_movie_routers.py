from fastapi import APIRouter, HTTPException, Query, Request, Query, Depends, status, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from schemas.movie import movie_list, MovieBase, MovieCreate, MovieUpdate, MoviePublic, MovieInDBBase
from models.movie import Movie
from models.genre import Genre
from models.review import Review
from sqlalchemy.orm import Session
from db.session import get_db
from services.movie_service import list_movie, get_movie_by_id, create_movie
from datetime import date


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse, name='movies')
async def movies(
    request: Request,
    db: Session = Depends(get_db),
    year: int = Query(None, description="Год выпуска"),
    # title: str = Query(None, description="Наименование фильма"),
    genre: str = Query(None, description="Наименование жанра"),
):
    """Вывод фильмов."""
    movie_db = list_movie(
        session=db,
        year_from=year,
        genre_name=genre,
    )

    context = {
        "request": request,
        "movies": movie_db,
        "user": 'Guest',
        "title": 'Список фильмов'
    }
    return templates.TemplateResponse("movies/movie_list.html", context=context)


@router.get("/{movie_id}/", response_class=HTMLResponse, name='html_movie_detail')
async def movie_detail(request: Request, movie_id: int, db: Session = Depends(get_db),):
    """Вывод одного фильма."""

    movie = get_movie_by_id(db, movie_id)

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Фильм c id {movie_id} не найден')

    context = {
        "request": request,
        "movie": movie,
        "user": 'Guest',
        # "title": movie.title
    }
    return templates.TemplateResponse("movies/movie_detail.html", context=context)


@router.get("/create", response_class=HTMLResponse, name="movies_html_create")
async def movie_create_form(request: Request):
    context = {
        "request": request,
        "errors": [],
        "form_data": {}
    }
    return templates.TemplateResponse("movies/movie_create.html", context=context)


@router.post("/create", name="movies_html_create_post")
async def movie_create(
    request: Request,
    db: Session = Depends(get_db),
    title: str = Form(...),
    year: int = Form(...),
    genre_name: str = Form(...),
    description: str = Form("")
):
    normilized_title = title.strip()
    normilized_genre_name = genre_name.strip()
    normilized_description = description.strip()

    form_data = {
        "title": normilized_title,
        "year": year,
        "genre_name": normilized_genre_name,
        "description": normilized_description
    }

    errors: list[str] = []

    if not normilized_title:
        errors.append("Название не может быть пустым")

    if len(normilized_title) > 100:
        errors.append("Название не может быть более 100")

    min_year = 1850
    max_year = date.today().year + 1
    if year > max_year:
        errors.append(f"Год не может быть больше {max_year}")

    if year < min_year:
        errors.append(f"Год не может быть меньше {min_year}")


    if errors:
        context = {
            "request": request,
            "errors": errors,
            "form_data": form_data,
        }
        return templates.TemplateResponse("movies/movie_create.html", context=context, status_code=status.HTTP_400_BAD_REQUEST)

    if normilized_genre_name is not None:
        genre = db.query(Genre).filter(Genre.name == genre_name).first()

        if genre is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Жанр  {genre_name} не найден')

    new_movie = create_movie(
        session=db,
        title=normilized_title,
        year=year,
        description=normilized_description,
        genre_name=normilized_genre_name
    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    redirect_url = request.url_for("movies")
    return RedirectResponse(url=redirect_url, status_code=status.HTTP_303_SEE_OTHER)
