# Exercício 3: Criar sistema de notas usando CSV

import csv

def criar_e_ler_csv():
    notas = [
        ["Aluno", "Nota"],
        ["Maria", 9.0],
        ["João", 7.5],
        ["Pedro", 8.3]
    ]

    # Criar CSV
    with open("exercicio3.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(notas)

    # Ler CSV
    print("\n=== Notas do CSV ===")
    with open("exercicio3.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for linha in reader:
            print(linha)

criar_e_ler_csv()
