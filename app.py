from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensaje": "¡Hola desde tu primera API en Railway!"})

@app.route("/status")
def status():
    return jsonify({"status": "OK", "version": "1.0"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
