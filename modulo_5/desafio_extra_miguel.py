# Exercício 4: Sistema de backup automático

import os
import shutil

def backup_automatico():
    origem = "origem_ex4"
    destino = "backup_ex4"

    # Criar pastas se não existirem
    os.makedirs(origem, exist_ok=True)
    os.makedirs(destino, exist_ok=True)

    # Criar arquivos de exemplo
    for i in range(1, 4):
        with open(f"{origem}/arquivo{i}.txt", "w") as f:
            f.write(f"Conteúdo do arquivo {i}")

    # Copiar arquivos
    for arquivo in os.listdir(origem):
        caminho_origem = os.path.join(origem, arquivo)
        caminho_destino = os.path.join(destino, arquivo)
        shutil.copy2(caminho_origem, caminho_destino)

    print("\n=== Backup Concluído ===")
    print("Arquivos copiados:", os.listdir(destino))

backup_automatico()
