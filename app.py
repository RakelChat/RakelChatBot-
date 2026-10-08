from flask import Flask, request, jsonify, render_template_string
import unicodedata
import re

app = Flask(__name__)

def normalizar(texto):
    texto = str(texto).lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"\s+", " ", texto)
    return texto


RESPOSTAS = {

# =========================
# CONVERSA
# =========================

"oi": "Oi! 😊 Eu sou o RakelChatBot. Como posso ajudar?",
"ola": "Olá! 😊 Eu sou o RakelChatBot. Como posso ajudar?",
"bom dia": "Bom dia! ☀️ Como posso ajudar?",
"boa tarde": "Boa tarde! 😊 Como posso ajudar?",
"boa noite": "Boa noite! 🌙 Como posso ajudar?",
"tudo bem": "Tudo bem por aqui! 😊 E com você?",
"qual seu nome": "Eu sou o RakelChatBot! 🤖",
"seu nome": "Meu nome é RakelChatBot. 🤖",
"quem e voce": "Sou o RakelChatBot, um chatbot criado para conversar e ajudar com perguntas.",
"o que voce faz": "Posso responder perguntas sobre matérias escolares, conhecimentos gerais, matemática, tecnologia e vários outros assuntos.",
"obrigado": "De nada! 😊",
"obrigada": "De nada! 😊",
"tchau": "Tchau! 👋 Até a próxima!",
"ate mais": "Até mais! 👋",
"voce e humano": "Não. Sou um programa de computador criado para conversar.",
"voce e uma ia": "Sou um chatbot criado para responder perguntas e conversar.",
"conte uma piada": "Por que o livro de matemática ficou triste? Porque tinha muitos problemas. 😂",
"me conte uma curiosidade": "Os polvos possuem três corações. 🐙",
"o que posso perguntar": "Você pode perguntar sobre Matemática, Português, História, Geografia, Biologia, Química, Física, Inglês, Educação Física, Filosofia, Sociologia, Astronomia, animais, tecnologia e conhecimentos gerais.",

# =========================
# INTELIGÊNCIA ARTIFICIAL E TECNOLOGIA
# =========================

"o que e inteligencia artificial": "Inteligência Artificial, ou IA, é uma tecnologia que permite aos computadores realizar tarefas que normalmente precisam de capacidades humanas, como analisar informações, reconhecer padrões e responder perguntas.",

"o que e ia": "IA significa Inteligência Artificial. Ela permite que computadores realizem tarefas de forma inteligente.",

"o que e chatbot": "Chatbot é um programa criado para conversar com pessoas por meio de mensagens.",

"o que e programacao": "Programação é o processo de criar instruções que dizem ao computador o que fazer.",

"o que e codigo": "Código é um conjunto de instruções escritas em uma linguagem de programação.",

"o que e algoritmo": "Algoritmo é uma sequência organizada de passos usada para resolver um problema ou realizar uma tarefa.",

"o que e internet": "A internet é uma grande rede que conecta computadores, celulares e outros dispositivos para trocar informações.",

"o que e tecnologia": "Tecnologia é o conjunto de conhecimentos, técnicas e ferramentas usados para resolver problemas e facilitar atividades.",

"o que e computador": "Computador é uma máquina capaz de receber, processar, armazenar e apresentar informações.",

"o que e celular": "Celular é um dispositivo eletrônico que permite comunicação, acesso à internet, aplicativos, câmera e várias outras funções.",

"o que e aplicativo": "Aplicativo é um programa criado para realizar determinadas funções em celulares, computadores ou outros dispositivos.",

"o que e site": "Site é um conjunto de páginas ou conteúdos que podem ser acessados pela internet.",

"o que e wifi": "Wi-Fi é uma tecnologia que permite conectar dispositivos a uma rede sem usar cabos.",

"o que e bluetooth": "Bluetooth é uma tecnologia usada para conectar dispositivos próximos sem fios.",

"o que e senha": "Senha é uma combinação usada para proteger contas, dispositivos e informações.",

"o que e robotica": "Robótica é a área da tecnologia que envolve a criação e utilização de robôs.",

"o que e ciberseguranca": "Cibersegurança é o conjunto de práticas usadas para proteger sistemas, dispositivos e informações digitais.",

"quem criou a internet": "A internet foi desenvolvida ao longo de décadas por vários pesquisadores e instituições.",

"quem criou a web": "Tim Berners-Lee criou a World Wide Web, conhecida como Web.",

# =========================
# MATEMÁTICA
# =========================

"quanto e 1 mais 1": "1 + 1 = 2.",
"quanto e 2 mais 2": "2 + 2 = 4.",
"quanto e 5 mais 5": "5 + 5 = 10.",
"quanto e 10 mais 10": "10 + 10 = 20.",
"quanto e 25 mais 25": "25 + 25 = 50.",
"quanto e 100 mais 50": "100 + 50 = 150.",

"quanto e 20 menos 7": "20 - 7 = 13.",
"quanto e 50 menos 20": "50 - 20 = 30.",
"quanto e 100 menos 35": "100 - 35 = 65.",

"quanto e 5 vezes 5": "5 × 5 = 25.",
"quanto e 10 vezes 5": "10 × 5 = 50.",
"quanto e 12 vezes 12": "12 × 12 = 144.",
"quanto e 7 vezes 8": "7 × 8 = 56.",
"quanto e 9 vezes 9": "9 × 9 = 81.",

"quanto e 100 dividido por 4": "100 ÷ 4 = 25.",
"quanto e 50 dividido por 5": "50 ÷ 5 = 10.",
"quanto e 81 dividido por 9": "81 ÷ 9 = 9.",

"quanto e 20 por cento de 100": "20% de 100 = 20.",
"quanto e 50 por cento de 100": "50% de 100 = 50.",
"quanto e 10 por cento de 200": "10% de 200 = 20.",

"o que e porcentagem": "Porcentagem é uma forma de representar uma parte de um total usando uma fração de 100.",

"o que e fracao": "Fração representa uma parte de um todo e possui numerador e denominador.",

"o que e numero primo": "Número primo é aquele que possui exatamente dois divisores positivos: 1 e ele mesmo.",

"o que e media": "Média aritmética é obtida somando os valores e dividindo o resultado pela quantidade de valores.",

"o que e geometria": "Geometria é a área da matemática que estuda formas, tamanhos, posições e medidas.",

"o que e perimetro": "Perímetro é a medida do contorno de uma figura.",

"o que e area": "Área é a medida da superfície ocupada por uma figura.",

"o que e equacao": "Equação é uma igualdade matemática que pode conter valores desconhecidos.",

"o que e raiz quadrada": "Raiz quadrada de um número é o valor que, multiplicado por ele mesmo, resulta nesse número.",

"qual a raiz quadrada de 25": "A raiz quadrada de 25 é 5.",

# =========================
# PORTUGUÊS
# =========================

"o que e substantivo": "Substantivo é a palavra usada para nomear pessoas, animais, lugares, objetos, sentimentos e ideias.",

"o que e verbo": "Verbo é a palavra que indica ação, estado ou fenômeno da natureza.",

"o que e adjetivo": "Adjetivo é a palavra que caracteriza ou dá uma qualidade a um substantivo.",

"o que e pronome": "Pronome é uma palavra que pode substituir ou acompanhar um substantivo.",

"o que e adverbio": "Advérbio é uma palavra que modifica principalmente um verbo, adjetivo ou outro advérbio.",

"o que e preposicao": "Preposição é uma palavra que liga termos e estabelece uma relação entre eles.",

"o que e sujeito": "Sujeito é o termo da oração sobre o qual se declara alguma coisa.",

"o que e predicado": "Predicado é a parte da oração que contém aquilo que se declara sobre o sujeito.",

"o que e frase": "Frase é um enunciado que possui sentido completo.",

"o que e oracao": "Oração é um enunciado que possui verbo ou locução verbal.",

"o que e sinonimo": "Sinônimos são palavras com significado igual ou parecido.",

"o que e antonimo": "Antônimos são palavras com significados opostos.",

"o que e metafora": "Metáfora é uma comparação implícita usada para dar um sentido figurado a uma expressão.",

"o que e literatura": "Literatura é a arte de usar a linguagem para criar obras como poemas, contos, romances e peças.",

"o que e poema": "Poema é um texto literário que pode utilizar versos, ritmo e diferentes formas de expressão.",

"o que e crase": "Crase é a fusão de dois 'a', geralmente a preposição a com o artigo a.",

# =========================
# HISTÓRIA
# =========================

"quem foi tiradentes": "Tiradentes foi um dos principais participantes da Inconfidência Mineira e é considerado um símbolo da luta pela independência do Brasil.",

"o que foi a inconfidencia mineira": "Foi um movimento ocorrido em Minas Gerais no século XVIII que defendia mudanças políticas e a separação de Portugal.",

"o que foi a revolucao industrial": "A Revolução Industrial foi um período de grandes mudanças na produção, marcado pelo crescimento das máquinas e das fábricas.",

"o que foi o iluminismo": "O Iluminismo foi um movimento intelectual que valorizou a razão, a liberdade, o conhecimento e a crítica às antigas estruturas políticas.",

"quem foi adam smith": "Adam Smith foi um pensador escocês considerado um dos principais nomes da economia clássica.",

"quem foi immanuel kant": "Immanuel Kant foi um filósofo alemão muito importante para o pensamento moderno e para o Iluminismo.",

"quem foi kant": "Immanuel Kant foi um filósofo alemão muito importante para o pensamento moderno e para o Iluminismo.",

"o que foi a primeira guerra mundial": "A Primeira Guerra Mundial ocorreu entre 1914 e 1918 e envolveu grandes potências e alianças internacionais.",

"o que foi a segunda guerra mundial": "A Segunda Guerra Mundial ocorreu entre 1939 e 1945 e envolveu países de vários continentes.",

"quando acabou a escravidao no brasil": "A escravidão foi abolida legalmente no Brasil em 13 de maio de 1888, com a Lei Áurea.",

"quem foi dom pedro primeiro": "Dom Pedro I foi o primeiro imperador do Brasil e declarou a independência do país em 1822.",

"quando foi a independencia do brasil": "A Independência do Brasil foi declarada em 7 de setembro de 1822.",

"quando foi proclamada a republica": "A República foi proclamada no Brasil em 15 de novembro de 1889.",

"o que foi a ditadura militar": "Foi um período da história do Brasil iniciado em 1964 e encerrado em 1985, marcado por governo militar e restrições políticas.",

"o que foi a idade media": "A Idade Média foi um período histórico europeu situado tradicionalmente entre a Antiguidade e a Idade Moderna.",

"o que foi o renascimento": "O Renascimento foi um movimento cultural que valorizou a arte, a ciência e o conhecimento.",

# =========================
# GEOGRAFIA
# =========================

"qual e a capital do brasil": "A capital do Brasil é Brasília.",

"qual e a capital da franca": "A capital da França é Paris.",

"qual e a capital da argentina": "A capital da Argentina é Buenos Aires.",

"qual e a capital dos estados unidos": "A capital dos Estados Unidos é Washington, D.C.",

"qual e a capital de portugal": "A capital de Portugal é Lisboa.",

"qual e a capital do japao": "A capital do Japão é Tóquio.",

"qual e a capital da italia": "A capital da Itália é Roma.",

"qual e a capital da inglaterra": "A capital da Inglaterra é Londres.",

"qual e o maior pais do mundo": "A Rússia é o maior país do mundo em área territorial.",

"qual e o maior estado do brasil": "O Amazonas é o maior estado brasileiro em área territorial.",

"o que e territorio": "Território é uma área delimitada que pode estar associada ao controle ou domínio de uma sociedade ou Estado.",

"o que e paisagem": "Paisagem é tudo aquilo que podemos observar em determinado espaço, incluindo elementos naturais e humanos.",

"o que e lugar": "Lugar é o espaço vivido pelas pessoas e carregado de experiências e relações.",

"o que e regiao": "Região é uma área que possui características comuns que permitem diferenciá-la de outras áreas.",

"o que e urbanizacao": "Urbanização é o crescimento da população e das atividades nas cidades.",

"o que e mobilidade urbana": "Mobilidade urbana é a forma como pessoas e mercadorias se deslocam dentro das cidades.",

"o que e globalizacao": "Globalização é o processo de aumento das conexões econômicas, culturais, tecnológicas e sociais entre diferentes partes do mundo.",

"o que e clima": "Clima é o conjunto de condições atmosféricas observadas em uma região durante longos períodos.",

"o que e tempo atmosferico": "Tempo atmosférico é o estado momentâneo da atmosfera em determinado lugar.",

"o que e relevo": "Relevo é o conjunto das formas da superfície terrestre, como montanhas, planaltos e planícies.",

"o que e hidrografia": "Hidrografia é o estudo e a descrição das águas de uma região, como rios, lagos e oceanos.",

# =========================
# BIOLOGIA
# =========================

"o que e celula": "Célula é a unidade básica que forma os seres vivos.",

"o que e dna": "DNA é a molécula que armazena informações genéticas dos seres vivos.",

"o que e gene": "Gene é uma unidade de informação genética presente no DNA.",

"o que e fotossintese": "Fotossíntese é o processo pelo qual plantas, algas e algumas bactérias produzem matéria orgânica usando luz.",

"o que e respiracao celular": "Respiração celular é o conjunto de processos usados pelas células para obter energia a partir de nutrientes.",

"o que e ecologia": "Ecologia é a área da Biologia que estuda as relações dos seres vivos entre si e com o ambiente.",

"o que e ecossistema": "Ecossistema é formado pelos seres vivos e pelos elementos não vivos que interagem em um ambiente.",

"o que e cadeia alimentar": "Cadeia alimentar representa a transferência de matéria e energia entre organismos por meio da alimentação.",

"o que e especie": "Espécie é um grupo de organismos com características semelhantes que pode produzir descendentes férteis em condições naturais.",

"o que e biodiversidade": "Biodiversidade é a variedade de seres vivos, genes e ecossistemas existentes.",

"o que e bacteria": "Bactéria é um organismo microscópico formado por uma célula sem núcleo delimitado.",

"o que e virus": "Vírus são agentes infecciosos que precisam de células hospedeiras para se multiplicar.",

"o que e sistema nervoso": "O sistema nervoso coordena e controla diversas funções do organismo e permite responder a estímulos.",

"o que e coracao": "O coração é um órgão muscular que bombeia o sangue pelo corpo.",

"quantos ossos tem o corpo humano": "Um adulto geralmente possui 206 ossos.",

"qual e o maior orgao do corpo humano": "A pele é o maior órgão do corpo humano.",

"o que e sangue": "Sangue é um tecido líquido que transporta gases, nutrientes, hormônios e resíduos pelo organismo.",

"o que e vacina": "Vacina é uma preparação que estimula o sistema imunológico a desenvolver proteção contra determinada doença.",

# =========================
# QUÍMICA
# =========================

"o que e quimica": "Química é a ciência que estuda a matéria, suas propriedades, transformações e interações.",

"o que e materia": "Matéria é tudo aquilo que possui massa e ocupa espaço.",

"o que e atomo": "Átomo é uma unidade básica da matéria, formada por um núcleo e elétrons.",

"o que e elemento quimico": "Elemento químico é um conjunto de átomos que possuem o mesmo número de prótons.",

"o que e molecula": "Molécula é uma estrutura formada por átomos ligados entre si.",

"o que e substancia": "Substância é uma forma de matéria com composição e propriedades características.",

"o que e mistura": "Mistura é formada por duas ou mais substâncias reunidas.",

"o que e ph": "pH é uma escala usada para indicar a acidez ou basicidade de uma solução.",

"o que e acido": "Ácido é uma substância que pode aumentar a concentração de íons hidrogênio em determinadas soluções.",

"o que e base": "Base é uma substância que pode aceitar prótons ou produzir íons hidróxido em determinadas soluções.",

"o que e reacao quimica": "Reação química é uma transformação em que substâncias são convertidas em outras substâncias.",

"o que sao propriedades coligativas": "Propriedades coligativas são propriedades de soluções que dependem principalmente da quantidade de partículas dissolvidas.",

"o que e evaporacao": "Evaporação é a passagem do estado líquido para o gasoso que ocorre na superfície de um líquido.",

"o que e fusao": "Fusão é a passagem do estado sólido para o líquido.",

# =========================
# FÍSICA
# =========================

"o que e fisica": "Física é a ciência que estuda fenômenos relacionados à matéria, energia, movimento, forças e interações.",

"o que e gravidade": "Gravidade é a interação que causa atração entre corpos com massa.",

"o que e velocidade": "Velocidade relaciona deslocamento e tempo e indica como a posição de um corpo muda.",

"o que e aceleracao": "Aceleração é a variação da velocidade ao longo do tempo.",

"o que e forca": "Força é uma interação capaz de alterar o movimento ou deformar um corpo.",

"o que e massa": "Massa é uma medida da quantidade de matéria de um corpo.",

"o que e peso": "Peso é a força gravitacional exercida sobre um corpo.",

"o que e energia": "Energia é uma grandeza associada à capacidade de produzir transformações.",

"o que e eletricidade": "Eletricidade está relacionada à presença e ao movimento de cargas elétricas.",

"o que e corrente eletrica": "Corrente elétrica é o movimento ordenado de cargas elétricas através de um material.",

"o que e luz": "Luz é uma forma de radiação eletromagnética que pode ser detectada pelo olho humano em determinada faixa.",

"o que e calor": "Calor é energia transferida entre corpos ou sistemas devido a uma diferença de temperatura.",

# =========================
# INGLÊS
# =========================

"como dizer ola em ingles": "Olá em inglês é Hello.",

"como dizer obrigado em ingles": "Obrigado em inglês é Thank you.",

"como dizer bom dia em ingles": "Bom dia em inglês é Good morning.",

"como dizer boa noite em ingles": "Boa noite em inglês pode ser Good night.",

"como dizer tchau em ingles": "Tchau em inglês é Bye.",

"como dizer por favor em ingles": "Por favor em inglês é Please.",

"como dizer sim em ingles": "Sim em inglês é Yes.",

"como dizer nao em ingles": "Não em inglês é No.",

"o que significa hello": "Hello significa Olá.",

"o que significa thank you": "Thank you significa Obrigado ou Obrigada.",

"o que significa good morning": "Good morning significa Bom dia.",

"o que significa good night": "Good night significa Boa noite.",

# =========================
# EDUCAÇÃO FÍSICA
# =========================

"o que e educacao fisica": "Educação Física estuda e trabalha práticas corporais, movimento, esportes, exercícios e saúde.",

"o que e exercicio fisico": "Exercício físico é uma atividade planejada e repetida com objetivo de melhorar ou manter a condição física.",

"o que e atividade fisica": "Atividade física é qualquer movimento corporal que aumenta o gasto de energia.",

"o que e resistencia": "Resistência é a capacidade de sustentar um esforço por determinado período.",

"o que e forca muscular": "Força muscular é a capacidade dos músculos de produzir tensão para realizar movimentos.",

"o que e flexibilidade": "Flexibilidade é a capacidade de realizar movimentos com determinada amplitude.",

"o que e treinamento": "Treinamento é um processo planejado de exercícios para desenvolver capacidades físicas ou habilidades.",

"principio da sobrecarga": "O princípio da sobrecarga indica que o organismo precisa receber estímulos adequados e progressivos para se adaptar.",

"principio da especificidade": "O princípio da especificidade indica que as adaptações dependem do tipo de estímulo realizado.",

"principio da individualidade": "O princípio da individualidade reconhece que cada pessoa responde de maneira diferente ao treinamento.",

"principio da continuidade": "O princípio da continuidade destaca a importância da regularidade para manter e desenvolver adaptações.",

# =========================
# FILOSOFIA E SOCIOLOGIA
# =========================

"o que e filosofia": "Filosofia é uma área do conhecimento que busca compreender questões fundamentais por meio da reflexão e da argumentação.",

"o que e sociologia": "Sociologia é a ciência que estuda a sociedade, as relações sociais e os grupos humanos.",

"o que e etica": "Ética é a reflexão sobre valores, princípios e comportamentos considerados corretos ou responsáveis.",

"o que e moral": "Moral é o conjunto de valores e normas que orientam comportamentos de uma pessoa ou sociedade.",

"quem foi socrates": "Sócrates foi um filósofo grego conhecido por seu método de questionamento e reflexão.",

"quem foi plato": "Platão foi um filósofo grego discípulo de Sócrates e fundador da Academia.",

"quem foi aristoteles": "Aristóteles foi um filósofo grego que estudou temas como lógica, ética, política e natureza.",

# =========================
# ASTRONOMIA
# =========================

"o que e astronomia": "Astronomia é a ciência que estuda os corpos celestes, o espaço e o Universo.",

"qual e o maior planeta": "Júpiter é o maior planeta do Sistema Solar.",

"qual e o menor planeta": "Mercúrio é o menor planeta do Sistema Solar.",

"qual e o planeta vermelho": "Marte é conhecido como planeta vermelho.",

"quantos planetas existem": "O Sistema Solar possui oito planetas.",

"qual e o satelite natural da terra": "A Lua é o satélite natural da Terra.",

"o que e estrela": "Estrela é um corpo celeste que produz sua própria luz e energia.",

"o que e planeta": "Planeta é um corpo celeste que orbita uma estrela e possui massa suficiente para ter formato aproximadamente arredondado.",

"o que e lua": "A Lua é o satélite natural da Terra.",

"o que e sol": "O Sol é a estrela localizada no centro do Sistema Solar.",

"o que e buraco negro": "Buraco negro é uma região do espaço com gravidade extremamente intensa.",

"o que e galaxia": "Galáxia é um grande conjunto de estrelas, gás, poeira e outros objetos ligados pela gravidade.",

"o que e universo": "Universo é tudo o que existe, incluindo espaço, tempo, matéria e energia.",

# =========================
# ANIMAIS E NATUREZA
# =========================

"qual e o maior animal do mundo": "A baleia-azul é o maior animal conhecido atualmente.",

"qual e o maior animal terrestre": "O elefante-africano é o maior animal terrestre.",

"qual e o animal mais rapido": "O falcão-peregrino é conhecido por atingir velocidades muito altas durante o mergulho.",

"onde vivem os pinguins": "A maioria das espécies de pinguins vive no Hemisfério Sul.",

"por que as abelhas sao importantes": "As abelhas são importantes principalmente porque ajudam na polinização de muitas plantas.",

"o que e polinizacao": "Polinização é a transferência de pólen que permite a reprodução de muitas plantas.",

"o que e floresta": "Floresta é uma área com grande presença de árvores e outras formas de vegetação.",

"o que e desmatamento": "Desmatamento é a retirada ou destruição de vegetação natural de uma área.",

# =========================
# MEIO AMBIENTE
# =========================

"o que e reciclagem": "Reciclagem é o processo de transformar materiais descartados em novos produtos ou matérias-primas.",

"o que e poluicao": "Poluição é a presença de agentes que podem prejudicar o ambiente e os seres vivos.",

"o que e efeito estufa": "Efeito estufa é um fenômeno natural que ajuda a manter a Terra aquecida. Sua intensificação contribui para o aquecimento global.",

"o que e aquecimento global": "Aquecimento global é o aumento da temperatura média do planeta associado principalmente ao aumento de gases de efeito estufa.",

"o que e sustentabilidade": "Sustentabilidade é buscar atender às necessidades atuais sem comprometer as possibilidades das futuras gerações.",

"como economizar agua": "Fechar a torneira quando não estiver usando, evitar desperdícios e consertar vazamentos são algumas atitudes úteis.",

"como ajudar o meio ambiente": "Reduzir desperdícios, reutilizar materiais, separar resíduos, economizar água e energia e cuidar das áreas verdes são atitudes importantes.",

# =========================
# CONHECIMENTOS GERAIS
# =========================

"qual e a moeda do brasil": "A moeda do Brasil é o real.",

"qual e a lingua oficial do brasil": "A língua oficial do Brasil é o português.",

"quantos estados tem o brasil": "O Brasil possui 26 estados e o Distrito Federal.",

"qual e o maior oceano": "O Oceano Pacífico é o maior oceano da Terra.",

"qual e o maior continente": "A Ásia é o maior continente em área.",

"quantos dias tem um ano": "Um ano comum tem 365 dias. Um ano bissexto tem 366.",

"quantos meses tem um ano": "Um ano tem 12 meses.",

"quantas horas tem um dia": "Um dia possui 24 horas.",

"quantos minutos tem uma hora": "Uma hora possui 60 minutos.",

"quantos segundos tem um minuto": "Um minuto possui 60 segundos.",

"qual e a estrela mais proxima da terra": "Depois do Sol, a estrela mais próxima da Terra é Proxima Centauri.",

"qual e o metal liquido em temperatura ambiente": "O mercúrio é um metal que permanece líquido em condições ambientes usuais.",

"qual e o simbolo quimico da agua": "A água é representada pela fórmula H₂O.",

"qual e o maior orgao do corpo humano": "A pele é o maior órgão do corpo humano.",

"quantos ossos tem um adulto": "Um adulto geralmente possui 206 ossos."

}


BANCO = {normalizar(k): v for k, v in RESPOSTAS.items()}


def encontrar_resposta(pergunta):

    p = normalizar(pergunta)

    if not p:
        return "Digite uma pergunta para eu responder. 😊"

    # Pergunta exata
    if p in BANCO:
        return BANCO[p]

    # Procura palavras-chave cadastradas
    for chave, resposta in BANCO.items():
        if len(chave) >= 6 and chave in p:
            return resposta

    # Conversas simples
    if p.startswith("oi") or p.startswith("ola"):
        return "Oi! 😊 Como posso ajudar?"

    if "seu nome" in p:
        return "Eu sou o RakelChatBot! 🤖"

    if "quem e voce" in p:
        return "Sou o RakelChatBot, seu chatbot escolar. 🤖"

    if "tchau" in p:
        return "Tchau! 👋 Até a próxima!"

    return (
        "Ainda estou aprendendo essa pergunta. 😊🤖\n\n"
        "Tente perguntar sobre Matemática, Português, História, "
        "Geografia, Biologia, Química, Física, Inglês, Educação Física, "
        "Filosofia, Sociologia, Astronomia, animais, tecnologia "
        "ou conhecimentos gerais."
    )


HTML = """
<!DOCTYPE html>
<html lang="pt-BR">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>RakelChatBot</title>

<style>

* {
    box-sizing: border-box;
}

body {

    margin: 0;

    font-family:
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    Arial,
    sans-serif;

    background: #f4f4f7;
}

header {

    background: #111827;

    color: white;

    padding: 18px 16px;

    text-align: center;
}

header h1 {

    margin: 0;

    font-size: 22px;
}

header p {

    margin: 5px 0 0;

    opacity: .8;

    font-size: 13px;
}

#chat {

    max-width: 760px;

    margin: auto;

    padding: 18px 14px 95px;
}

.msg {

    max-width: 86%;

    padding: 12px 14px;

    border-radius: 16px;

    margin: 10px 0;

    line-height: 1.45;

    white-space: pre-wrap;
}

.user {

    margin-left: auto;

    background: #2563eb;

    color: white;

    border-bottom-right-radius: 5px;
}

.bot {

    margin-right: auto;

    background: white;

    color: #111827;

    border-bottom-left-radius: 5px;

    box-shadow:
    0 1px 4px rgba(0,0,0,.08);
}

form {

    position: fixed;

    left: 0;
    right: 0;
    bottom: 0;

    background: white;

    padding: 10px;

    border-top: 1px solid #ddd;

    display: flex;

    gap: 8px;
}

form div {

    max-width: 760px;

    width: 100%;

    margin: auto;

    display: flex;

    gap: 8px;
}

input {

    flex: 1;

    border: 1px solid #ccc;

    border-radius: 22px;

    padding: 12px 15px;

    font-size: 16px;

    outline: none;
}

button {

    border: 0;

    border-radius: 22px;

    background: #2563eb;

    color: white;

    padding: 0 18px;

    font-size: 15px;
}

button:disabled {

    opacity: .6;
}

</style>

</head>

<body>

<header>

<h1>RakelChatBot 🤖</h1>

<p>
Chatbot escolar para perguntas e respostas
</p>

</header>


<div id="chat">

<div class="msg bot">

Oi! 😊 Eu sou o RakelChatBot.
Como posso ajudar?

</div>

</div>


<form id="form">

<div>

<input
id="mensagem"
autocomplete="off"
placeholder="Digite sua pergunta..."
>

<button id="enviar">

Enviar

</button>

</div>

</form>


<script>

const chat =
document.getElementById("chat");

const form =
document.getElementById("form");

const input =
document.getElementById("mensagem");

const botao =
document.getElementById("enviar");


function adicionarMensagem(
    texto,
    classe
) {

    const div =
    document.createElement("div");

    div.className =
    "msg " + classe;

    div.textContent =
    texto;

    chat.appendChild(div);

    window.scrollTo(
        0,
        document.body.scrollHeight
    );
}


form.addEventListener(
    "submit",
    async function(e) {

        e.preventDefault();

        const mensagem =
        input.value.trim();

        if (!mensagem) {
            return;
        }

        adicionarMensagem(
            mensagem,
            "user"
        );

        input.value = "";

        botao.disabled = true;


        try {

            const resposta =
            await fetch(
                "/chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body:
                    JSON.stringify({
                        mensagem:
                        mensagem
                    })
                }
            );


            const dados =
            await resposta.json();


            adicionarMensagem(
                dados.resposta ||
                "Não consegui responder.",
                "bot"
            );


        } catch (erro) {

            adicionarMensagem(
                "Ops! Não consegui falar com o servidor. Tente novamente. 😕",
                "bot"
            );

        } finally {

            botao.disabled = false;

            input.focus();

        }

    }
);

</script>

</body>

</html>
"""


@app.get("/")
def inicio():

    return render_template_string(
        HTML
    )


@app.post("/chat")
def chat():

    dados =
    request.get_json(
        silent=True
    ) or {}

    mensagem =
    dados.get(
        "mensagem",
        ""
    )

    return jsonify({

        "resposta":
        encontrar_resposta(
            mensagem
        )

    })


if __name__ == "__main__":

    app.run()
