# clients.py

from database import get_connection


def inserir_cliente(nome, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))

    conn.commit()
    conn.close()


def consultar_clientes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Clientes")
    resultados = cursor.fetchall()

    conn.close()
    return resultados


def atualizar_cliente(id_cliente, novo_nome, novo_email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Clientes
        SET nome = ?, email = ?
        WHERE id = ?
    """, (novo_nome, novo_email, id_cliente))

    conn.commit()
    conn.close()


def deletar_cliente(id_cliente):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))

    conn.commit()
    conn.close()


def filtrar_por_letra(letra):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Clientes WHERE nome LIKE ?", (f"{letra}%",))
    resultados = cursor.fetchall()

    conn.close()
    return resultados
