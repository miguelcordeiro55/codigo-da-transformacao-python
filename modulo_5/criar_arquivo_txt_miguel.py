# Exercício 1: Criar um arquivo .txt, gravar e ler informações

import os

def criar_arquivo_txt():
    conteudo = "Olá! Este é um arquivo .txt criado pelo Python.\nLinha 2 do arquivo."

    # Gravar
    with open("exercicio1.txt", "w", encoding="utf-8") as txt:
        txt.write(conteudo)

    # Ler
    with open("exercicio1.txt", "r", encoding="utf-8") as txt:
        print("\n=== Conteúdo do TXT ===")
        print(txt.read())

criar_arquivo_txt()
