from flask import Blueprint

saudacao_bp = Blueprint("saudacao", __name__)

@saudacao_bp.route("/saudacao", methods=["GET"])
def saudacao():
    return {"mensagem": "Olá! Bem-vindo à API Flask!"}
