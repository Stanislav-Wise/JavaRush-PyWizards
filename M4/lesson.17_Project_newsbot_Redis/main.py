import uvicorn
from fastapi import FastAPI
from app.config import settings
from app.api import router


app = FastAPI(
    title="Newsbot Telegram",
    version="0.3.0"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)