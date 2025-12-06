# validacao.py

def validar_idade(idade):
    try:
        idade = int(idade)
        if idade <= 0:
            raise ValueError("A idade deve ser um número positivo.")
        return idade
    except ValueError:
        return "Erro: idade inválida, digite um número inteiro positivo."