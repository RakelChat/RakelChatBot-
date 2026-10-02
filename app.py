from flask import Flask, request, jsonify, render_template_string

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

    elif "capital do brasil" in mensagem:
        return "A capital do Brasil é Brasília! 🇧🇷"

    elif "planeta" in mensagem:
        return "A Terra é o planeta onde vivemos. 🌎"

    elif "fotossíntese" in mensagem or "fotossintese" in mensagem:
        return "Fotossíntese é o processo em que as plantas usam luz para produzir seu próprio alimento. 🌱☀️"

    elif "matemática" in mensagem or "matematica" in mensagem:
        return "A matemática estuda números, formas, medidas e relações. 🔢📐"

    elif mensagem == "tchau":
        return "Até mais! 👋"

    else:
        return "Ainda estou aprendendo, mas vou ficar cada vez melhor! 😊"


@app.route("/", methods=["GET"])
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RakelChatBot</title>

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f3e8ff;
}

header {
    background: #7c3aed;
    color: white;
    padding: 18px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

#chat {
    height: calc(100vh - 140px);
    overflow-y: auto;
    padding: 20px;
}

.mensagem {
    padding: 12px 16px;
    margin: 10px 0;
    border-radius: 18px;
    max-width: 75%;
}

.usuario {
    background: #7c3aed;
    color: white;
    margin-left: auto;
}

.bot {
    background: white;
    color: #333;
    margin-right: auto;
}

form {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    padding: 12px;
    background: white;
    box-shadow: 0 -2px 10px #ccc;
}

input {
    flex: 1;
    padding: 14px;
    border: 1px solid #ccc;
    border-radius: 25px;
    font-size: 16px;
}

button {
    margin-left: 8px;
    padding: 0 20px;
    border: none;
    border-radius: 25px;
    background: #7c3aed;
    color: white;
    font-size: 16px;
}
</style>
</head>

<body>

<header>🤖 RakelChatBot</header>

<div id="chat">
    <div class="mensagem bot">
        Oi! 😊 Eu sou o RakelChatBot. Como posso ajudar?
    </div>
</div>

<form id="form">
    <input id="mensagem" placeholder="Digite uma mensagem..." autocomplete="off">
    <button type="submit">Enviar</button>
</form>

<script>
const form = document.getElementById("form");
const input = document.getElementById("mensagem");
const chat = document.getElementById("chat");

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const mensagem = input.value.trim();

    if (!mensagem) return;

    chat.innerHTML += `
        <div class="mensagem usuario">${mensagem}</div>
    `;

    input.value = "";

    const resposta = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ mensagem: mensagem })
    });

    const dados = await resposta.json();

    chat.innerHTML += `
        <div class="mensagem bot">${dados.resposta}</div>
    `;

    chat.scrollTop = chat.scrollHeight;
});
</script>

</body>
</html>
    """)


@app.post("/chat")
def chat():
    dados = request.get_json(silent=True) or {}
    mensagem = dados.get("mensagem", "")
    return jsonify({"resposta": responder(mensagem)})
