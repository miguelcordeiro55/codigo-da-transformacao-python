from flask import Blueprint, request, jsonify
from models.usuario import inserir_usuario, listar_usuarios

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return {"erro": "Campos nome e email são obrigatórios."}, 400

    try:
        inserir_usuario(nome, email)
        return {"mensagem": "Usuário cadastrado com sucesso!"}, 201
    except Exception as e:
        return {"erro": str(e)}, 500


@usuarios_bp.route("/usuarios", methods=["GET"])
def listar():
    lista = listar_usuarios()

    usuarios = [
        {"id": item[0], "nome": item[1], "email": item[2]}
        for item in lista
    ]

    return jsonify(usuarios)
