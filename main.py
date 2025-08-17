from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Holaap Busca un manga!"}

