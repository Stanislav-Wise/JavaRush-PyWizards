import uvicorn
from fastapi import FastAPI
from routers.main_routers import router as main_router
from routers.movie_routers import router as movie_router
from routers.html_movie_routers import router as html_movie_router


app = FastAPI()
app.include_router(main_router, tags=["Main"])
app.include_router(html_movie_router, tags=["html movies"], prefix="/movies")
app.include_router(movie_router, tags=["api movies"], prefix="/api/v2/movies")



if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)