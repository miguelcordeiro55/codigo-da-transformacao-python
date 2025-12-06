# api.py

from flask import Flask, jsonify, request # type: ignore

app = Flask(__name__)


@app.get("/soma")
def soma():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify({"resultado": a + b})


@app.get("/divide")
def divide():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 1))
    if b == 0:
        return jsonify({"erro": "Divisão por zero"}), 400
    return jsonify({"resultado": a / b})


if __name__ == "__main__":
    app.run(debug=True)
