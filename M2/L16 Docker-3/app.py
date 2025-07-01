import uvicorn
from fastapi import FastAPI, Request, HTTPException


app = FastAPI()

@app.get("/")
async def cmd_index():
    return {'message': 'Hello FastAPI'}


@app.get("/about/")
async def cmd_about():
    return {'message': 'Hello JavaRush!!!'}


# uvicorn app:app --reload --host localhost --port 8001
if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)