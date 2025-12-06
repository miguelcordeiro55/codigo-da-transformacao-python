# main.py

from calculadora import dividir
from banco import ContaBancaria, SaldoInsuficienteErro
from validacão import validar_idade
from login import sistema_login

def main():
    print("\n=== Testando a calculadora ===")
    print(dividir(10, 2))
    print(dividir(5, 0))

    print("\n=== Testando conta bancária ===")
    conta = ContaBancaria(100)
    try:
        print("Novo saldo:", conta.sacar(30))
        print("Novo saldo:", conta.sacar(100))  # vai causar exceção
    except SaldoInsuficienteErro as e:
        print(e)

    print("\n=== Validando idade ===")
    print(validar_idade("20"))
    print(validar_idade("-5"))
    print(validar_idade("abc"))

    print("\n=== Sistema de Login ===")
    print(sistema_login("admin", "1234"))

if __name__ == "_main_":
    main()