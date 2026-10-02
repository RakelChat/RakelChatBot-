from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)


def responder(mensagem):
    mensagem = mensagem.lower().strip()

    # CONVERSA
    if mensagem in ["oi", "olá", "ola", "oie", "oii", "oláá"]:
        return "Oi! 😊 Eu sou o RakelChatBot. Como posso ajudar?"

    elif "seu nome" in mensagem:
        return "Meu nome é RakelChatBot! 🤖"

    elif "quem criou você" in mensagem or "quem te criou" in mensagem:
        return "Eu fui criado pela Rakel como um projeto de chatbot. 💜🤖"

    elif "quem é você" in mensagem:
        return "Eu sou o RakelChatBot, um chatbot criado para conversar, ensinar e responder perguntas. 🤖"

    elif "tudo bem" in mensagem:
        return "Tudo bem por aqui! 😊 E com você?"

    elif "obrigado" in mensagem or "obrigada" in mensagem:
        return "Por nada! 😊"

    elif mensagem in ["tchau", "até mais", "ate mais"]:
        return "Até mais! 👋💜"

    # MATEMÁTICA
    elif "o que é matemática" in mensagem or "o que e matematica" in mensagem:
        return "Matemática é a área que estuda números, formas, medidas, quantidades e relações. 🔢"

    elif "quanto é 2+2" in mensagem or "quanto e 2+2" in mensagem:
        return "2 + 2 = 4. 🧮"

    elif "quanto é 5+5" in mensagem or "quanto e 5+5" in mensagem:
        return "5 + 5 = 10. 🧮"

    elif "quanto é 10-5" in mensagem or "quanto e 10-5" in mensagem:
        return "10 - 5 = 5. 🧮"

    # PORTUGUÊS
    elif "o que é substantivo" in mensagem or "o que e substantivo" in mensagem:
        return "Substantivo é a palavra que dá nome a pessoas, lugares, objetos, animais, sentimentos e outras coisas. 📖"

    elif "o que é verbo" in mensagem or "o que e verbo" in mensagem:
        return "Verbo é uma palavra que indica ação, estado ou fenômeno, como correr, estudar e ser. 📚"

    elif "o que é adjetivo" in mensagem or "o que e adjetivo" in mensagem:
        return "Adjetivo é a palavra que caracteriza ou dá uma qualidade a um substantivo. ✏️"

    # HISTÓRIA
    elif "o que foi o iluminismo" in mensagem or "o que foi iluminismo" in mensagem:
        return "O Iluminismo foi um movimento intelectual dos séculos XVII e XVIII que valorizava a razão, a ciência e a liberdade. 💡"

    elif "quem foi tiradentes" in mensagem:
        return "Tiradentes foi um dos participantes da Inconfidência Mineira e se tornou um símbolo da história do Brasil. 🇧🇷"

    elif "independência do brasil" in mensagem or "independencia do brasil" in mensagem:
        return "A Independência do Brasil foi proclamada em 7 de setembro de 1822. 🇧🇷"

    # GEOGRAFIA
    elif "capital do brasil" in mensagem:
        return "A capital do Brasil é Brasília. 🇧🇷"

    elif "maior país do mundo" in mensagem or "maior pais do mundo" in mensagem:
        return "O maior país do mundo em área territorial é a Rússia. 🌎"

    elif "o que é geografia" in mensagem or "o que e geografia" in mensagem:
        return "Geografia é a área que estuda o espaço, os lugares, a natureza e a relação das pessoas com o ambiente. 🌎"

    # BIOLOGIA
    elif "o que é célula" in mensagem or "o que e celula" in mensagem:
        return "A célula é a unidade básica que forma os seres vivos. 🔬"

    elif "o que é fotossíntese" in mensagem or "o que e fotossintese" in mensagem:
        return "Fotossíntese é o processo pelo qual as plantas usam luz, água e gás carbônico para produzir seu alimento. 🌱☀️"

    elif "o que é dna" in mensagem or "o que e dna" in mensagem:
        return "O DNA é uma molécula que armazena informações genéticas dos seres vivos. 🧬"

    # QUÍMICA
    elif "o que é átomo" in mensagem or "o que e atomo" in mensagem:
        return "Átomo é uma unidade básica da matéria, formada por partículas como prótons, nêutrons e elétrons. ⚛️"

    elif "o que é química" in mensagem or "o que e quimica" in mensagem:
        return "Química é a ciência que estuda a matéria, suas propriedades, transformações e interações. 🧪"

    # FÍSICA
    elif "o que é física" in mensagem or "o que e fisica" in mensagem:
        return "Física é a ciência que estuda fenômenos como movimento, força, energia, luz, calor e eletricidade. ⚡"

    elif "velocidade" in mensagem:
        return "Velocidade indica quão rápido um objeto se desloca. Uma fórmula comum é velocidade = distância ÷ tempo. 🚗"

    # INGLÊS
    elif "como fala oi em inglês" in mensagem or "como fala oi em ingles" in mensagem:
        return "Oi em inglês é 'Hi' ou 'Hello'. 🇺🇸"

    elif "como fala obrigado em inglês" in mensagem or "como fala obrigado em ingles" in mensagem:
        return "Obrigado em inglês é 'Thank you'. 🇺🇸"

    elif "como fala escola em inglês" in mensagem or "como fala escola em ingles" in mensagem:
        return "Escola em inglês é 'school'. 📚🇺🇸"

    # EDUCAÇÃO FÍSICA
    elif "o que é exercício físico" in mensagem or "o que e exercicio fisico" in mensagem:
        return "Exercício físico é uma atividade corporal planejada que pode ajudar na saúde, força, resistência e bem-estar. 🏃"

    elif "o que é esporte" in mensagem or "o que e esporte" in mensagem:
        return "Esporte é uma atividade física organizada, geralmente com regras e objetivos. ⚽"

    # CIÊNCIA E NATUREZA
    elif "quantos planetas existem" in mensagem:
        return "O Sistema Solar possui oito planetas. 🪐"

    elif "qual é o planeta onde vivemos" in mensagem or "qual e o planeta onde vivemos" in mensagem:
        return "Nós vivemos no planeta Terra. 🌎"

    elif "o que é água" in mensagem or "o que e agua" in mensagem:
        return "A água é uma substância essencial para a vida e é formada por hidrogênio e oxigênio. 💧"

    elif "animal mais rápido" in mensagem or "animal mais rapido" in mensagem:
        return "O falcão-peregrino é conhecido por atingir velocidades muito altas durante o voo de mergulho. 🦅"

    # TECNOLOGIA
    elif "o que é internet" in mensagem or "o que e internet" in mensagem:
        return "A internet é uma rede mundial que conecta computadores, celulares e outros dispositivos. 🌐"

    elif "o que é inteligência artificial" in mensagem or "o que e inteligencia artificial" in mensagem:
        return "Inteligência artificial é uma tecnologia que permite a sistemas de computador realizar tarefas que normalmente exigem capacidades humanas, como analisar informações e gerar respostas. 🤖"

    # CURIOSIDADES
    elif "curiosidade" in mensagem:
        return "Uma curiosidade: os polvos possuem três corações. 🐙❤️"

    elif "me conte uma curiosidade" in mensagem:
        return "Uma curiosidade: a luz do Sol leva cerca de 8 minutos para chegar à Terra. ☀️🌎"

    elif "conte uma piada" in mensagem or "me conta uma piada" in mensagem:
        return "Por que o livro de matemática ficou triste? Porque tinha muitos problemas! 😂📚"

    else:
        return "Ainda estou aprendendo! 😊 Tente perguntar sobre Matemática, História, Geografia, Ciências, Português, Inglês, Química, Física, tecnologia ou conhecimentos gerais."


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


if __name__ == "__main__":
    app.run()
