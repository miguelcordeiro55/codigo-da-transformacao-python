from flask import Flask
from routes.saudacao import saudacao_bp
from routes.usuarios import usuarios_bp
from database.conexao import criar_tabela

def create_app():
    app = Flask(__name__)

    # Registrar Blueprints
    app.register_blueprint(saudacao_bp)
    app.register_blueprint(usuarios_bp)

    # Criar tabela no banco
    criar_tabela()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
