# tasks.py

from database import get_connection


def adicionar_tarefa(descricao):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Tarefas (descricao) VALUES (?)", (descricao,))
    conn.commit()
    conn.close()


def listar_tarefas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Tarefas")
    resultados = cursor.fetchall()

    conn.close()
    return resultados


def deletar_tarefa(id_tarefa):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
