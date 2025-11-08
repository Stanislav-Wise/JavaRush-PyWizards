from fastapi import APIRouter


router = APIRouter()


@router.get("/")
@router.get("/home/")
async def index():
    """Главная страница."""
    return {"message": "Hello World!!!"}


@router.get("/about/")
async def about():
    """Страница о нас."""
    return {"message": "Страница о нас."}
