from database.conexao import conectar

def inserir_usuario(nome, email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, email FROM usuarios")
    resultados = cursor.fetchall()

    conn.close()
    return resultados
