from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Holaap Busca un manga!"}

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
