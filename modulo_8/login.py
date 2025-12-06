# login.py

def sistema_login(usuario_correto, senha_correta):
    tentativas = 3

    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            return "Login realizado com sucesso!"
        
        tentativas -= 1
        print(f"Credenciais inválidas! Tentativas restantes: {tentativas}")

    return "Acesso bloqueado! Muitas tentativas incorretas."