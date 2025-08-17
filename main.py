from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hola! Busca tu manga favorito!"}  #This is the message that you´ll see in the root


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
