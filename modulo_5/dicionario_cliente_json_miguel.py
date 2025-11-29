# Exercício 2: Salve e carregue um dicionário de clientes em JSON

import json

def salvar_e_ler_json():
    clientes = {
        "cliente1": {"nome": "Ana", "idade": 28},
        "cliente2": {"nome": "Carlos", "idade": 35},
        "cliente3": {"nome": "Julia", "idade": 22}
    }

    # Salvar JSON
    with open("exercicio2.json", "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

    # Ler JSON
    with open("exercicio2.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    print("\n=== Dados do JSON ===")
    print(dados)

salvar_e_ler_json()
