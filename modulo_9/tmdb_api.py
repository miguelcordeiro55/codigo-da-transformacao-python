# tmdb_api.py

import requests # type: ignore
from config import TMDB_API_KEY

BASE_URL = "https://api.themoviedb.org/3/search/movie"


def buscar_filme(titulo: str):
    try:
        params = {
            "api_key": TMDB_API_KEY,
            "language": "pt-BR",
            "query": titulo
        }

        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()

        if not data["results"]:
            return {"erro": "Nenhum filme encontrado."}

        filme = data["results"][0]

        return {
            "titulo": filme["title"],
            "sinopse": filme["overview"],
            "nota": filme["vote_average"],
            "data_lancamento": filme["release_date"]
        }

    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro ao consultar TMDB: {e}"}
