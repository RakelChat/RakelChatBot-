from flask import Flask, request, jsonify, render_template_string
import unicodedata

app = Flask(__name__)


# =========================================================
# FUNÇÕES
# =========================================================

def normalizar(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto


def contem(mensagem, palavras):
    return any(palavra in mensagem for palavra in palavras)


# =========================================================
# RAKELCHATBOT
# =========================================================

def responder(mensagem):
    original = mensagem
    mensagem = normalizar(mensagem)

    # -----------------------------------------------------
    # CONVERSA
    # -----------------------------------------------------

    if mensagem in ["oi", "ola", "oie", "oii", "e ai", "eai", "hey"]:
        return "Oi! 😊 Eu sou o RakelChatBot. Como posso ajudar?"

    if "seu nome" in mensagem:
        return "Meu nome é RakelChatBot! 🤖💜"

    if "quem e voce" in mensagem:
        return "Eu sou o RakelChatBot, um chatbot criado para conversar, ensinar e responder perguntas. 🤖"

    if "quem criou voce" in mensagem or "quem te criou" in mensagem:
        return "Eu fui criado pela Rakel como um projeto de chatbot. 💜🤖"

    if "tudo bem" in mensagem or "como voce esta" in mensagem:
        return "Tudo bem por aqui! 😊 E com você?"

    if "obrigado" in mensagem or "obrigada" in mensagem:
        return "Por nada! 😊💜"

    if mensagem in ["tchau", "ate mais", "adeus"]:
        return "Até mais! 👋💜"

    if "bom dia" in mensagem:
        return "Bom dia! ☀️😊"

    if "boa tarde" in mensagem:
        return "Boa tarde! 🌤️😊"

    if "boa noite" in mensagem:
        return "Boa noite! 🌙😊"


    # -----------------------------------------------------
    # MATEMÁTICA
    # -----------------------------------------------------

    if contem(mensagem, ["o que e matematica", "matematica"]):
        return "Matemática é a área que estuda números, quantidades, formas, medidas, relações e padrões. 🔢"

    if contem(mensagem, ["fracao", "fracoes"]):
        return "Fração representa uma parte de um todo. Ela possui numerador, que fica em cima, e denominador, que fica embaixo. 🧮"

    if contem(mensagem, ["porcentagem", "por cento"]):
        return "Porcentagem representa uma parte de 100. Por exemplo, 25% significa 25 partes em cada 100."

    if contem(mensagem, ["regra de tres", "regra de 3"]):
        return "A regra de três é usada para descobrir um valor desconhecido quando existe uma relação de proporção entre grandezas."

    if contem(mensagem, ["equacao", "equacoes"]):
        return "Equação é uma igualdade que possui um ou mais valores desconhecidos, geralmente representados por letras."

    if contem(mensagem, ["potenciacao", "potencia"]):
        return "Potenciação é uma multiplicação de fatores iguais. Em 2³, por exemplo, o 2 é a base e o 3 é o expoente."

    if contem(mensagem, ["raiz quadrada", "radiciacao"]):
        return "A raiz quadrada de um número é o valor que, multiplicado por ele mesmo, produz esse número. √25 = 5."

    if contem(mensagem, ["area do quadrado"]):
        return "A área de um quadrado é calculada multiplicando o lado por ele mesmo: A = lado × lado."

    if contem(mensagem, ["perimetro"]):
        return "Perímetro é a medida do contorno de uma figura. Para encontrá-lo, somamos o comprimento de todos os lados."

    if "quanto e 2+2" in mensagem or "quanto e 2 + 2" in mensagem:
        return "2 + 2 = 4. 🧮"

    if "quanto e 5+5" in mensagem or "quanto e 5 + 5" in mensagem:
        return "5 + 5 = 10. 🧮"

    if "quanto e 10-5" in mensagem or "quanto e 10 - 5" in mensagem:
        return "10 - 5 = 5. 🧮"


    # -----------------------------------------------------
    # PORTUGUÊS
    # -----------------------------------------------------

    if contem(mensagem, ["substantivo"]):
        return "Substantivo é a palavra que dá nome a pessoas, animais, lugares, objetos, sentimentos e outras coisas."

    if contem(mensagem, ["verbo"]):
        return "Verbo é a palavra que indica ação, estado ou fenômeno, como correr, estudar, ser e chover."

    if contem(mensagem, ["adjetivo"]):
        return "Adjetivo é a palavra que caracteriza ou dá uma qualidade a um substantivo."

    if contem(mensagem, ["pronome"]):
        return "Pronome é uma palavra que pode substituir ou acompanhar um substantivo, como eu, você, ele, ela e nós."

    if contem(mensagem, ["adverbio"]):
        return "Advérbio é uma palavra que modifica o sentido de um verbo, adjetivo ou outro advérbio, indicando circunstâncias como tempo, lugar ou modo."

    if contem(mensagem, ["preposicao"]):
        return "Preposição é uma palavra que liga termos e estabelece uma relação entre eles, como de, para, com, em e por."

    if contem(mensagem, ["sujeito"]):
        return "Sujeito é o termo da oração sobre o qual se declara alguma coisa."

    if contem(mensagem, ["predicado"]):
        return "Predicado é a parte da oração que apresenta uma informação sobre o sujeito."

    if contem(mensagem, ["pontuacao", "pontuacoes"]):
        return "Pontuação organiza o texto e ajuda a indicar pausas e sentidos. Exemplos: ponto, vírgula, dois-pontos, ponto de interrogação e exclamação."


    # -----------------------------------------------------
    # HISTÓRIA
    # -----------------------------------------------------

    if contem(mensagem, ["iluminismo"]):
        return "O Iluminismo foi um movimento intelectual dos séculos XVII e XVIII que valorizava a razão, a ciência, a liberdade e a crítica ao poder absoluto."

    if contem(mensagem, ["revolucao francesa"]):
        return "A Revolução Francesa começou em 1789 e provocou grandes mudanças políticas e sociais na França."

    if contem(mensagem, ["revolucao industrial"]):
        return "A Revolução Industrial começou na Inglaterra no século XVIII e trouxe máquinas, fábricas e grandes mudanças na produção e na sociedade."

    if contem(mensagem, ["independencia do brasil"]):
        return "A Independência do Brasil foi proclamada em 7 de setembro de 1822, durante o processo liderado por Dom Pedro."

    if contem(mensagem, ["tiradentes"]):
        return "Tiradentes foi participante da Inconfidência Mineira e tornou-se uma figura importante da história do Brasil."

    if contem(mensagem, ["inconfidencia mineira"]):
        return "A Inconfidência Mineira foi um movimento ocorrido em Minas Gerais no final do século XVIII contra o domínio colonial português."

    if contem(mensagem, ["escravidao", "escravidao no brasil"]):
        return "A escravidão marcou profundamente a história do Brasil. Milhões de africanos foram trazidos à força para trabalhar, principalmente na agricultura e na mineração."

    if contem(mensagem, ["primeira guerra mundial"]):
        return "A Primeira Guerra Mundial aconteceu entre 1914 e 1918 e envolveu diversas potências e alianças internacionais."

    if contem(mensagem, ["segunda guerra mundial"]):
        return "A Segunda Guerra Mundial aconteceu entre 1939 e 1945 e envolveu países de diferentes continentes."

    if contem(mensagem, ["guerra fria"]):
        return "A Guerra Fria foi uma disputa política, econômica, militar e ideológica principalmente entre Estados Unidos e União Soviética após a Segunda Guerra Mundial."


    # -----------------------------------------------------
    # GEOGRAFIA
    # -----------------------------------------------------

    if contem(mensagem, ["capital do brasil"]):
        return "A capital do Brasil é Brasília. 🇧🇷"

    if contem(mensagem, ["maior pais do mundo"]):
        return "O maior país do mundo em área territorial é a Rússia. 🌎"

    if contem(mensagem, ["continentes"]):
        return "Os continentes são grandes extensões de terras emersas. Na divisão mais usada no Brasil, temos América, Europa, Ásia, África, Oceania e Antártida."

    if contem(mensagem, ["oceanos"]):
        return "Os cinco oceanos são: Atlântico, Pacífico, Índico, Glacial Ártico e Glacial Antártico."

    if contem(mensagem, ["clima"]):
        return "Clima é o conjunto das condições atmosféricas que caracterizam uma região durante longos períodos."

    if contem(mensagem, ["tempo atmosferico"]):
        return "Tempo atmosférico é o estado momentâneo da atmosfera, como chuva, temperatura, vento e umidade."

    if contem(mensagem, ["globalizacao"]):
        return "Globalização é o processo de aumento das conexões entre diferentes partes do mundo, envolvendo economia, cultura, tecnologia e comunicação."

    if contem(mensagem, ["urbanizacao"]):
        return "Urbanização é o crescimento das cidades e o aumento da população vivendo em áreas urbanas."


    # -----------------------------------------------------
    # BIOLOGIA E CIÊNCIAS
    # -----------------------------------------------------

    if contem(mensagem, ["celula", "celulas"]):
        return "A célula é a unidade básica que forma os seres vivos. 🔬"

    if contem(mensagem, ["fotossintese"]):
        return "Fotossíntese é o processo pelo qual plantas, algas e alguns microrganismos usam luz para produzir matéria orgânica a partir de água e gás carbônico. 🌱☀️"

    if contem(mensagem, ["dna"]):
        return "O DNA é uma molécula que armazena informações genéticas dos seres vivos. 🧬"

    if contem(mensagem, ["genetica"]):
        return "Genética é a área da Biologia que estuda a hereditariedade e a transmissão das características dos seres vivos."

    if contem(mensagem, ["ecossistema"]):
        return "Ecossistema é o conjunto formado pelos seres vivos e pelos elementos não vivos de determinado ambiente, com suas relações."

    if contem(mensagem, ["cadeia alimentar"]):
        return "Cadeia alimentar representa a transferência de matéria e energia entre os seres vivos por meio da alimentação."

    if contem(mensagem, ["evolucao"]):
        return "Evolução biológica é o processo de mudança das populações de seres vivos ao longo das gerações."

    if contem(mensagem, ["o que e biologica", "biologia"]):
        return "Biologia é a ciência que estuda os seres vivos e suas relações."

    if contem(mensagem, ["corpo humano"]):
        return "O corpo humano é formado por sistemas que trabalham juntos, como os sistemas respiratório, digestório, circulatório e nervoso."


    # -----------------------------------------------------
    # QUÍMICA
    # -----------------------------------------------------

    if contem(mensagem, ["atomo", "atomos"]):
        return "Átomo é uma unidade básica da matéria. Ele possui prótons, nêutrons e elétrons. ⚛️"

    if contem(mensagem, ["molecula", "moleculas"]):
        return "Molécula é uma estrutura formada por dois ou mais átomos ligados quimicamente."

    if contem(mensagem, ["tabela periodica"]):
        return "A Tabela Periódica organiza os elementos químicos de acordo com suas propriedades e características."

    if contem(mensagem, ["ligacao quimica", "ligacoes quimicas"]):
        return "Ligações químicas são interações que unem átomos. Entre os principais tipos estão as ligações iônica, covalente e metálica."

    if contem(mensagem, ["mistura", "misturas"]):
        return "Mistura é a união de duas ou mais substâncias sem que elas necessariamente formem uma nova substância."

    if contem(mensagem, ["ph"]):
        return "pH é uma escala usada para indicar se uma solução é ácida, neutra ou básica."

    if contem(mensagem, ["propriedades coligativas"]):
        return "Propriedades coligativas são propriedades das soluções que dependem principalmente da quantidade de partículas de soluto presentes."


    # -----------------------------------------------------
    # FÍSICA
    # -----------------------------------------------------

    if contem(mensagem, ["fisica"]):
        return "Física é a ciência que estuda fenômenos como movimento, força, energia, luz, calor e eletricidade. ⚡"

    if contem(mensagem, ["velocidade"]):
        return "Velocidade indica quão rápido um objeto se desloca. Uma fórmula comum é v = distância ÷ tempo."

    if contem(mensagem, ["forca"]):
        return "Força é uma interação capaz de alterar o movimento de um objeto ou causar uma deformação."

    if contem(mensagem, ["energia"]):
        return "Energia é a capacidade de realizar trabalho ou provocar transformações. Existem diferentes formas de energia."

    if contem(mensagem, ["gravidade"]):
        return "Gravidade é a interação que provoca atração entre corpos que possuem massa."

    if contem(mensagem, ["eletricidade"]):
        return "Eletricidade está relacionada à presença e ao movimento de cargas elétricas."


    # -----------------------------------------------------
    # INGLÊS
    # -----------------------------------------------------

    if contem(mensagem, ["oi em ingles", "oi em ingles"]):
        return "Oi em inglês pode ser 'Hi' ou 'Hello'. 🇺🇸"

    if contem(mensagem, ["obrigado em ingles"]):
        return "Obrigado em inglês é 'Thank you'. 🇺🇸"

    if contem(mensagem, ["escola em ingles"]):
        return "Escola em inglês é 'school'. 📚"

    if contem(mensagem, ["casa em ingles"]):
        return "Casa em inglês pode ser 'house' ou 'home', dependendo do contexto."

    if contem(mensagem, ["amigo em ingles"]):
        return "Amigo em inglês é 'friend'."

    if contem(mensagem, ["como voce esta em ingles"]):
        return "Como você está? = 'How are you?'"

    if contem(mensagem, ["bom dia em ingles"]):
        return "Bom dia em inglês é 'Good morning'. ☀️"


    # -----------------------------------------------------
    # EDUCAÇÃO FÍSICA
    # -----------------------------------------------------

    if contem(mensagem, ["exercicio fisico"]):
        return "Exercício físico é uma atividade corporal planejada que pode contribuir para saúde, força, resistência e bem-estar."

    if contem(mensagem, ["esporte"]):
        return "Esporte é uma atividade física organizada, geralmente praticada com regras e objetivos."

    if contem(mensagem, ["treinamento desportivo"]):
        return "O treinamento desportivo utiliza princípios como individualidade, sobrecarga, adaptação, continuidade e especificidade."

    if contem(mensagem, ["aquecimento"]):
        return "Aquecimento é uma preparação realizada antes da atividade física para preparar o corpo para o exercício."


    # -----------------------------------------------------
    # FILOSOFIA E SOCIOLOGIA
    # -----------------------------------------------------

    if contem(mensagem, ["filosofia"]):
        return "Filosofia é uma área do conhecimento que busca compreender questões fundamentais sobre existência, conhecimento, ética, sociedade e realidade."

    if contem(mensagem, ["sociologia"]):
        return "Sociologia é a ciência que estuda a sociedade, as relações sociais, os grupos e as instituições."

    if contem(mensagem, ["socrates"]):
        return "Sócrates foi um filósofo grego conhecido por utilizar o diálogo e os questionamentos como forma de buscar conhecimento."

    if contem(mensagem, ["platao"]):
        return "Platão foi um filósofo grego, discípulo de Sócrates e professor de Aristóteles."

    if contem(mensagem, ["aristoteles"]):
        return "Aristóteles foi um filósofo grego que estudou diversos campos, como lógica, ética, política, natureza e ciência."


    # -----------------------------------------------------
    # ASTRONOMIA
    # -----------------------------------------------------

    if contem(mensagem, ["quantos planetas", "planetas existem"]):
        return "O Sistema Solar possui oito planetas. 🪐"

    if contem(mensagem, ["planeta onde vivemos", "onde vivemos"]):
        return "Nós vivemos no planeta Terra. 🌎"

    if contem(mensagem, ["sol"]):
        return "O Sol é uma estrela localizada no centro do Sistema Solar. ☀️"

    if contem(mensagem, ["lua"]):
        return "A Lua é o satélite natural da Terra. 🌙"

    if contem(mensagem, ["sistema solar"]):
        return "O Sistema Solar é formado pelo Sol e pelos corpos celestes que orbitam ao seu redor, incluindo oito planetas."


    # -----------------------------------------------------
    # ANIMAIS E NATUREZA
    # -----------------------------------------------------

    if contem(mensagem, ["animal mais rapido"]):
        return "O falcão-peregrino é conhecido por atingir velocidades extremamente altas durante o voo de mergulho. 🦅"

    if contem(mensagem, ["polvo"]):
        return "Uma curiosidade: os polvos possuem três corações. 🐙❤️"

    if contem(mensagem, ["abelha"]):
        return "As abelhas são importantes polinizadoras e ajudam na reprodução de muitas plantas. 🐝"

    if contem(mensagem, ["dinossauro"]):
        return "Os dinossauros viveram durante milhões de anos antes da existência dos seres humanos. 🦖"

    if contem(mensagem, ["meio ambiente"]):
        return "O meio ambiente inclui os seres vivos, os elementos naturais e as relações entre eles."


    # -----------------------------------------------------
    # TECNOLOGIA
    # -----------------------------------------------------

    if contem(mensagem, ["internet"]):
        return "A internet é uma grande rede que conecta computadores, celulares e outros dispositivos no mundo inteiro. 🌐"

    if contem(mensagem, ["inteligencia artificial"]):
        return "Inteligência artificial é uma tecnologia que permite a computadores realizar tarefas que normalmente exigem capacidades humanas, como analisar informações e gerar respostas. 🤖"

    if contem(mensagem, ["programacao"]):
        return "Programação é o processo de criar instruções para que um computador execute determinadas tarefas."

    if contem(mensagem, ["python"]):
        return "Python é uma linguagem de programação conhecida por sua sintaxe relativamente simples e muito utilizada em projetos de tecnologia, ciência e automação."

    if contem(mensagem, ["aplicativo", "app"]):
        return "Um aplicativo é um programa criado para realizar determinadas funções em um dispositivo."


    # -----------------------------------------------------
    # BRASIL
    # -----------------------------------------------------

    if contem(mensagem, ["brasil"]):
        return "O Brasil é um país localizado na América do Sul e possui 26 estados e o Distrito Federal. 🇧🇷"

    if contem(mensagem, ["capital de sao paulo"]):
        return "A capital do estado de São Paulo é São Paulo."

    if contem(mensagem, ["capital do maranhao"]):
        return "A capital do Maranhão é São Luís. 🇧🇷"

    if contem(mensagem, ["regioes do brasil"]):
        return "O Brasil é dividido em cinco grandes regiões: Norte, Nordeste, Centro-Oeste, Sudeste e Sul."


    # -----------------------------------------------------
    # CURIOSIDADES
    # -----------------------------------------------------

    if contem(mensagem, ["curiosidade", "curiosidades"]):
        return "Curiosidade: os polvos possuem três corações! 🐙❤️"

    if contem(mensagem, ["me conte uma curiosidade", "conta uma curiosidade"]):
        return "A luz do Sol leva aproximadamente 8 minutos para chegar à Terra. ☀️🌎"

    if contem(mensagem, ["piada", "conte uma piada", "conta uma piada"]):
        return "Por que o livro de matemática ficou triste? Porque tinha muitos problemas! 😂📚"


    # -----------------------------------------------------
    # RESPOSTA PADRÃO
    # -----------------------------------------------------

    return (
        "Ainda estou aprendendo! 😊🤖\n\n"
        "Você pode perguntar sobre:\n"
        "📚 Matemática, Português, História, Geografia, Biologia, "
        "Química, Física, Inglês, Filosofia, Sociologia e Educação Física.\n"
        "🌎 Países, animais, espaço, natureza e conhecimentos gerais.\n"
        "💻 Tecnologia, internet e programação.\n"
        "💬 Ou simplesmente conversar comigo!"
    )


# =========================================================
# SITE
# =========================================================

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
    white-space: pre-line;
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
Oi! 😊 Eu sou o RakelChatBot.
<br>
Posso ajudar com matérias escolares, conhecimentos gerais, tecnologia, curiosidades e muito mais! 💜
</div>

</div>

<form id="form">

<input
id="mensagem"
placeholder="Digite uma mensagem..."
autocomplete="off"
>

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
        <div class="mensagem usuario">
            ${mensagem}
        </div>
    `;

    input.value = "";

    const resposta = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            mensagem: mensagem
        })

    });

    const dados = await resposta.json();

    chat.innerHTML += `
        <div class="mensagem bot">
            ${dados.resposta}
        </div>
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

    resposta = responder(mensagem)

    return jsonify({
        "resposta": resposta
    })


if __name__ == "__main__":
    app.run()
