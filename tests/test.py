import requests

BASE_URL = "http://127.0.0.1:8000"

def test_manga(title):
    url = f"{BASE_URL}/manga/{title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            manga = data["data"][0]
            title = manga.get("title", "Sin título")
            authors = [a["name"] for a in manga.get("authors", [])]
            genres = [g["name"] for g in manga.get("genres", [])]
            score = manga.get("score", "N/A")
            url = manga.get("url", None)
            
            print(f" Manga encontrado: {title}")
            print(f"Autores: {', '.join(authors)}")
            print(f"Géneros: {', '.join(genres)}")
            print(f"Puntaje: {score}")
            print(f"URL: {url}")
        else:
            print(f" Manga '{title}' no encontrado")
    else:
        print(f" Error {response.status_code} al buscar manga '{title}'")

if __name__ == "__main__":
    test_manga("Berserk")