import random
import math

print("=== Jogo de Adivinhação ===")
numero_secreto = random.randint(1, 100)

tentativas = 0
chute = -1

while chute != numero_secreto:
    chute = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    diferenca = abs(numero_secreto - chute)

    if chute < numero_secreto:
        print("Muito baixo!")
    elif chute > numero_secreto:
        print("Muito alto!")

    # Dica usando math
    print("Dica: você está a",
          math.ceil(diferenca / 2), "passos do número correto!")

print(f"Parabéns! Você acertou em {tentativas} tentativas!")