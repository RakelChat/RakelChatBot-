from flask import Flask, request, jsonify

app = Flask(__name__)

def responder(mensagem):
    mensagem = mensagem.lower().strip()

    if mensagem in ["oi", "olá", "ola"]:
        return "Oi! 😊 Eu sou o RakelChatBot. Como posso ajudar?"

    elif "seu nome" in mensagem:
        return "Meu nome é RakelChatBot! 🤖"

    elif "tudo bem" in mensagem:
        return "Tudo bem por aqui! E com você? 😊"

    elif "quem é você" in mensagem:
        return "Eu sou um chatbot criado para conversar e responder perguntas. 🤖"

    elif mensagem == "tchau":
        return "Até mais! 👋"

    else:
        return "Ainda estou aprendendo, mas vou ficar cada vez melhor! 😊"

@app.get("/")
def home():
    return "RakelChatBot está online! 🤖"

@app.post("/chat")
def chat():
    dados = request.get_json(silent=True) or {}
    mensagem = dados.get("mensagem", "")
    return jsonify({"resposta": responder(mensagem)})
