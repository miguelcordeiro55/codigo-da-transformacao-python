# main.py

from weather_api import get_weather
from tmdb_api import buscar_filme  # opcional

print("=== Consulta ao Clima ===")
cidade = input("Digite o nome da cidade: ")

resultado_clima = get_weather(cidade)

if "erro" in resultado_clima:
    print("Erro:", resultado_clima["erro"])
else:
    print(f"\nClima em {resultado_clima['cidade']}:")
    print(f"Temperatura: {resultado_clima['temperatura']}°C")
    print(f"Sensação térmica: {resultado_clima['sensacao']}°C")
    print(f"Condições: {resultado_clima['condicoes']}")

# -----------------------------
# Desafio extra: Buscar filme
# -----------------------------
print("\n=== Busca de Filme (TMDB) ===")
titulo = input("Digite o nome de um filme: ")

resultado_filme = buscar_filme(titulo)

if "erro" in resultado_filme:
    print("Erro:", resultado_filme["erro"])
else:
    print(f"\nTítulo: {resultado_filme['titulo']}")
    print(f"Sinopse: {resultado_filme['sinopse']}")
    print(f"Nota: {resultado_filme['nota']}")
    print(f"Lançamento: {resultado_filme['data_lancamento']}")
