from fastapi import FastAPI
import requests
from fastapi.responses import JSONResponse
from fastapi.requests import Request

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "API is running"}


@app.get("/")
def root():
    return {
        "msg": "Hola! Busca un manga o anime usando /manga/{title} o /anime/{title}",
        "usage_example": {
            "manga": "/manga/berserk",
            "anime": "/anime/naruto"
        }
    }


@app.get("/manga/{title}")
def get_manga(title: str):
    url = f"https://api.jikan.moe/v4/manga?q={title}&limit=1"
    r = requests.get(url)
    return r.json()

@app.get("/anime/{title}")
def get_anime(title: str):
    url = f"https://api.jikan.moe/v4/anime?q={title}&limit=1"
    r = requests.get(url)
    return r.json()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)}
    )