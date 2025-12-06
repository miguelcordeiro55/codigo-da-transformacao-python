# main.py

from database import create_tables
import clients
import tasks

def menu():
    print("\n=== Sistema de Clientes ===")
    print("1 - Inserir cliente")
    print("2 - Consultar clientes")
    print("3 - Atualizar cliente")
    print("4 - Deletar cliente")
    print("5 - Filtrar nomes começando com uma letra")
    print("6 - Gerenciar tarefas (Desafio Extra)")
    print("0 - Sair")


def menu_tarefas():
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Deletar tarefa")
    print("0 - Voltar")


def main():
    create_tables()

    while True:
        menu()
        opc = input("Escolha: ")

        if opc == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            clients.inserir_cliente(nome, email)
            print("Cliente inserido!")

        elif opc == "2":
            for c in clients.consultar_clientes():
                print(c)

        elif opc == "3":
            idc = input("ID do cliente: ")
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            clients.atualizar_cliente(idc, nome, email)
            print("Atualizado!")

        elif opc == "4":
            idc = input("ID do cliente: ")
            clients.deletar_cliente(idc)
            print("Deletado!")

        elif opc == "5":
            letra = input("Letra inicial: ")
            filtrados = clients.filtrar_por_letra(letra.upper())
            for c in filtrados:
                print(c)

        elif opc == "6":
            while True:
                menu_tarefas()
                escolha = input("Escolha: ")

                if escolha == "1":
                    desc = input("Descrição da tarefa: ")
                    tasks.adicionar_tarefa(desc)

                elif escolha == "2":
                    for t in tasks.listar_tarefas():
                        print(t)

                elif escolha == "3":
                    idt = input("ID da tarefa: ")
                    tasks.deletar_tarefa(idt)

                elif escolha == "0":
                    break

        elif opc == "0":
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
