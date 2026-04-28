from flask import Flask, jsonify

app = Flask(__name__)

# página inicial
@app.route('/')
def hello():
    return "olá! API funcionando."

# função de soma
def somar(a, b):
    return a + b

# função de subtração
def subtrair(a, b):
    return a - b

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)