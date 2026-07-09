from flask import Flask, render_template, request, jsonify
from assistant_core import generar_respuesta

app = Flask(__name__)

historial = [{"role": "system", "content": "Bienvenido, soy tu asistente virtual."}]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", historial=historial)


@app.route("/chat", methods=["POST"])
def chat():
    mensaje = request.json.get("message", "").strip()
    if not mensaje:
        return jsonify(success=False, message="Mensaje vacio")

    historial.append({"role": "user", "content": mensaje})
    mensajes_para_ia = [m for m in historial if m["role"] in ("user", "assistant")]
    respuesta = generar_respuesta(mensajes_para_ia)

    historial.append({"role": "assistant", "content": respuesta})
    return jsonify(success=True, message=respuesta)


@app.route("/reset", methods=["POST"])
def reset():
    historial.clear()
    historial.append({"role": "system", "content": "Bienvenido, soy tu asistente virtual."})
    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True)