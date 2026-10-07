from flask import Flask, request, jsonify, render_template_string
import unicodedata
import re

app = Flask(__name__)

# =========================================================
# BANCO DE PERGUNTAS E RESPOSTAS
# Para adicionar uma resposta:
# "pergunta": "resposta",
# =========================================================
RESPOSTAS = {
    'o que é matemática?': 'Matemática é a área que estuda números, quantidades, formas, medidas, relações e padrões.',
    'o que é uma fração?': 'Fração representa uma parte de um todo. O número de cima é o numerador e o de baixo é o denominador.',
    'o que é porcentagem?': 'Porcentagem representa uma parte de 100. Por exemplo, 25% significa 25 em cada 100.',
    'o que é uma equação?': 'Equação é uma igualdade que possui um ou mais valores desconhecidos.',
    'o que é regra de três?': 'Regra de três é um método usado para descobrir um valor desconhecido quando existe uma relação de proporção.',
    'quanto é 2 + 2?': '2 + 2 = 4.',
    'quanto é 5 + 5?': '5 + 5 = 10.',
    'quanto é 10 - 5?': '10 - 5 = 5.',
    'quanto é 6 x 7?': '6 × 7 = 42.',
    'quanto é 100 dividido por 4?': '100 ÷ 4 = 25.',
    'o que é perímetro?': 'Perímetro é a medida do contorno de uma figura, obtida somando seus lados.',
    'o que é área?': 'Área é a medida da superfície de uma figura.',
    'qual é a área de um quadrado?': 'A área de um quadrado é lado × lado.',
    'o que é média aritmética?': 'É o resultado da soma dos valores dividida pela quantidade de valores.',
    'o que é potência?': 'Potenciação é uma multiplicação de fatores iguais.',
    'o que é raiz quadrada?': 'É o número que, multiplicado por ele mesmo, produz o número original. √25 = 5.',
    'o que é substantivo?': 'Substantivo é a palavra que dá nome a pessoas, animais, lugares, objetos, sentimentos e outras coisas.',
    'o que é verbo?': 'Verbo é a palavra que indica ação, estado ou fenômeno.',
    'o que é adjetivo?': 'Adjetivo é a palavra que caracteriza ou dá uma qualidade a um substantivo.',
    'o que é pronome?': 'Pronome é uma palavra que pode substituir ou acompanhar um substantivo.',
    'o que é advérbio?': 'Advérbio modifica o sentido de um verbo, adjetivo ou outro advérbio.',
    'o que é preposição?': 'Preposição liga palavras e estabelece uma relação entre elas.',
    'o que é sujeito?': 'Sujeito é o termo da oração sobre o qual se declara alguma coisa.',
    'o que é predicado?': 'Predicado é a parte da oração que apresenta uma informação sobre o sujeito.',
    'o que é pontuação?': 'Pontuação organiza o texto e ajuda a indicar pausas e sentidos.',
    'o que é uma oração?': 'Oração é uma frase que normalmente possui um verbo ou uma locução verbal.',
    'o que é sinônimo?': 'Sinônimos são palavras com significado igual ou parecido.',
    'o que é antônimo?': 'Antônimos são palavras com significados opostos.',
    'o que é metáfora?': 'Metáfora é uma comparação implícita usada para criar um sentido figurado.',
    'o que é interpretação de texto?': 'É compreender as informações, ideias e sentidos presentes em um texto.',
    'o que foi o iluminismo?': 'O Iluminismo foi um movimento intelectual dos séculos XVII e XVIII que valorizava a razão, a ciência e a liberdade.',
    'quem foi adam smith?': 'Adam Smith foi um filósofo e economista escocês considerado um dos principais pensadores do liberalismo econômico.',
    'quem foi immanuel kant?': 'Immanuel Kant foi um filósofo alemão ligado ao Iluminismo e conhecido por seus estudos sobre razão, conhecimento e ética.',
    'o que foi a revolução francesa?': 'A Revolução Francesa começou em 1789 e provocou grandes mudanças políticas e sociais na França.',
    'o que foi a revolução industrial?': 'A Revolução Industrial começou na Inglaterra no século XVIII e trouxe máquinas, fábricas e mudanças na produção.',
    'quando foi a independência do brasil?': 'A Independência do Brasil foi proclamada em 7 de setembro de 1822.',
    'quem proclamou a independência do brasil?': 'Dom Pedro proclamou a Independência do Brasil em 7 de setembro de 1822.',
    'quem foi tiradentes?': 'Tiradentes participou da Inconfidência Mineira e tornou-se uma importante figura da história do Brasil.',
    'o que foi a inconfidência mineira?': 'Foi um movimento ocorrido em Minas Gerais no final do século XVIII contra o domínio colonial português.',
    'o que foi a escravidão no brasil?': 'Foi um sistema de exploração que submeteu milhões de pessoas, principalmente africanos e seus descendentes, à escravidão.',
    'quando foi abolida a escravidão no brasil?': 'A escravidão foi abolida legalmente no Brasil em 13 de maio de 1888.',
    'o que foi a primeira guerra mundial?': 'A Primeira Guerra Mundial aconteceu de 1914 a 1918 e envolveu grandes potências e alianças internacionais.',
    'o que foi a segunda guerra mundial?': 'A Segunda Guerra Mundial aconteceu de 1939 a 1945 e envolveu países de vários continentes.',
    'o que foi a guerra fria?': 'Foi uma disputa política, econômica, militar e ideológica principalmente entre Estados Unidos e União Soviética.',
    'quem foi dom pedro ii?': 'Dom Pedro II foi o segundo e último imperador do Brasil.',
    'qual é a capital do brasil?': 'A capital do Brasil é Brasília.',
    'qual é a capital do maranhão?': 'A capital do Maranhão é São Luís.',
    'quais são as regiões do brasil?': 'Norte, Nordeste, Centro-Oeste, Sudeste e Sul.',
    'quantos estados tem o brasil?': 'O Brasil possui 26 estados e o Distrito Federal.',
    'qual é o maior país do mundo?': 'A Rússia é o maior país do mundo em área territorial.',
    'o que é globalização?': 'Globalização é o aumento das conexões entre diferentes partes do mundo na economia, cultura, tecnologia e comunicação.',
    'o que é urbanização?': 'Urbanização é o crescimento das cidades e o aumento da população vivendo em áreas urbanas.',
    'o que é clima?': 'Clima é o conjunto das condições atmosféricas de uma região observado durante longos períodos.',
    'o que é tempo atmosférico?': 'Tempo atmosférico é o estado momentâneo da atmosfera, como chuva, temperatura, vento e umidade.',
    'o que é migração?': 'Migração é o deslocamento de pessoas de um lugar para outro.',
    'o que é população?': 'População é o conjunto de pessoas que vivem em determinado lugar.',
    'o que é território?': 'Território é uma área delimitada sobre a qual existe controle ou domínio.',
    'o que é paisagem?': 'Paisagem é tudo aquilo que podemos perceber de um espaço, incluindo elementos naturais e humanos.',
    'quais são os continentes?': 'Na divisão mais usada no Brasil, são América, Europa, Ásia, África, Oceania e Antártida.',
    'quais são os oceanos?': 'Atlântico, Pacífico, Índico, Glacial Ártico e Glacial Antártico.',
    'o que é uma célula?': 'A célula é a unidade básica que forma os seres vivos.',
    'o que é fotossíntese?': 'Fotossíntese é o processo pelo qual plantas, algas e alguns microrganismos usam luz para produzir matéria orgânica.',
    'o que é dna?': 'DNA é uma molécula que armazena informações genéticas dos seres vivos.',
    'o que é genética?': 'Genética é a área da Biologia que estuda a hereditariedade e a transmissão de características.',
    'o que é ecossistema?': 'Ecossistema é o conjunto formado pelos seres vivos e pelos elementos não vivos de um ambiente e suas relações.',
    'o que é cadeia alimentar?': 'Cadeia alimentar representa a transferência de matéria e energia entre seres vivos por meio da alimentação.',
    'o que é evolução biológica?': 'É o processo de mudança das populações de seres vivos ao longo das gerações.',
    'o que é biologia?': 'Biologia é a ciência que estuda os seres vivos e suas relações.',
    'o que é sistema nervoso?': 'É o sistema responsável por receber informações, processá-las e coordenar várias funções do corpo.',
    'o que é sistema respiratório?': 'É o sistema responsável pelas trocas de gases, principalmente pela entrada de oxigênio e saída de gás carbônico.',
    'o que é sistema digestório?': 'É o conjunto de órgãos responsável pela digestão dos alimentos e absorção de nutrientes.',
    'o que é fotossíntese e por que ela é importante?': 'Ela permite que plantas produzam seu alimento e contribui para a produção de oxigênio e para o equilíbrio dos ecossistemas.',
    'o que são animais vertebrados?': 'São animais que possuem coluna vertebral.',
    'o que são animais invertebrados?': 'São animais que não possuem coluna vertebral.',
    'o que é um átomo?': 'Átomo é uma unidade básica da matéria formada por partículas como prótons, nêutrons e elétrons.',
    'o que é uma molécula?': 'Molécula é uma estrutura formada por dois ou mais átomos ligados quimicamente.',
    'o que é a tabela periódica?': 'A Tabela Periódica organiza os elementos químicos de acordo com suas propriedades.',
    'o que é ligação química?': 'É uma interação que une átomos. Os principais tipos são iônica, covalente e metálica.',
    'o que é uma mistura?': 'Mistura é a união de duas ou mais substâncias.',
    'o que é ph?': 'pH é uma escala usada para indicar se uma solução é ácida, neutra ou básica.',
    'o que são propriedades coligativas?': 'São propriedades das soluções que dependem principalmente da quantidade de partículas de soluto.',
    'o que é ácido?': 'Ácido é uma substância que apresenta características químicas relacionadas à liberação de íons hidrogênio em solução aquosa.',
    'o que é base?': 'Base é uma substância que apresenta características químicas associadas à aceitação de prótons ou produção de íons hidróxido em determinadas soluções.',
    'o que é reação química?': 'É uma transformação em que substâncias iniciais dão origem a novas substâncias.',
    'o que é física?': 'Física é a ciência que estuda fenômenos como movimento, força, energia, luz, calor e eletricidade.',
    'o que é velocidade?': 'Velocidade indica quão rápido um objeto se desloca. Uma fórmula comum é v = distância ÷ tempo.',
    'o que é força?': 'Força é uma interação capaz de alterar o movimento de um objeto ou causar deformação.',
    'o que é energia?': 'Energia é a capacidade de realizar trabalho ou provocar transformações.',
    'o que é gravidade?': 'Gravidade é a interação que provoca atração entre corpos que possuem massa.',
    'o que é eletricidade?': 'Eletricidade está relacionada à presença e ao movimento de cargas elétricas.',
    'o que é temperatura?': 'Temperatura indica o estado térmico de um corpo e está relacionada à agitação das partículas.',
    'o que é pressão?': 'Pressão relaciona uma força aplicada a uma determinada área.',
    'como se diz oi em inglês?': "Oi em inglês pode ser 'Hi' ou 'Hello'.",
    'como se diz obrigado em inglês?': "Obrigado em inglês é 'Thank you'.",
    'como se diz escola em inglês?': "Escola em inglês é 'school'.",
    'como se diz casa em inglês?': "Casa pode ser 'house' ou 'home', dependendo do contexto.",
    'como se diz amigo em inglês?': "Amigo em inglês é 'friend'.",
    'como se diz como você está em inglês?': "Como você está? = 'How are you?'",
    'como se diz bom dia em inglês?': "Bom dia = 'Good morning'.",
    'como se diz boa noite em inglês?': "Boa noite = 'Good night'.",
    'o que é exercício físico?': 'Exercício físico é uma atividade corporal planejada que pode contribuir para saúde, força, resistência e bem-estar.',
    'o que é esporte?': 'Esporte é uma atividade física organizada, geralmente praticada com regras e objetivos.',
    'o que é treinamento desportivo?': 'Treinamento desportivo utiliza princípios como individualidade, sobrecarga, adaptação, continuidade e especificidade.',
    'o que é aquecimento?': 'Aquecimento é uma preparação realizada antes da atividade física.',
    'o que é resistência física?': 'Resistência é a capacidade de sustentar uma atividade física durante determinado período.',
    'o que é força muscular?': 'Força muscular é a capacidade dos músculos de produzir tensão para realizar uma ação.',
    'o que é filosofia?': 'Filosofia busca compreender questões fundamentais sobre existência, conhecimento, ética, sociedade e realidade.',
    'o que é sociologia?': 'Sociologia é a ciência que estuda a sociedade, as relações sociais, os grupos e as instituições.',
    'quem foi sócrates?': 'Sócrates foi um filósofo grego conhecido pelo uso do diálogo e dos questionamentos.',
    'quem foi platão?': 'Platão foi um filósofo grego, discípulo de Sócrates e professor de Aristóteles.',
    'quem foi aristóteles?': 'Aristóteles foi um filósofo grego que estudou lógica, ética, política, natureza e ciência.',
    'quantos planetas existem no sistema solar?': 'O Sistema Solar possui oito planetas.',
    'qual é o planeta onde vivemos?': 'Nós vivemos no planeta Terra.',
    'o que é o sol?': 'O Sol é uma estrela localizada no centro do Sistema Solar.',
    'o que é a lua?': 'A Lua é o satélite natural da Terra.',
    'o que é o sistema solar?': 'O Sistema Solar é formado pelo Sol e pelos corpos celestes que orbitam ao seu redor.',
    'o que é um eclipse solar?': 'É um fenômeno em que a Lua passa entre a Terra e o Sol e bloqueia parte da luz solar para determinadas regiões.',
    'o que é uma estrela?': 'Estrela é um corpo celeste que produz sua própria luz e energia.',
    'qual é o animal mais rápido?': 'O falcão-peregrino é conhecido por atingir velocidades extremamente altas durante seu voo de mergulho.',
    'quantos corações tem um polvo?': 'Um polvo possui três corações.',
    'por que as abelhas são importantes?': 'As abelhas são importantes polinizadoras e ajudam na reprodução de muitas plantas.',
    'o que são dinossauros?': 'Dinossauros foram um grupo diverso de répteis que viveu na Terra por milhões de anos.',
    'o que é meio ambiente?': 'Meio ambiente inclui os seres vivos, os elementos naturais e as relações entre eles.',
    'o que é internet?': 'Internet é uma grande rede que conecta computadores, celulares e outros dispositivos no mundo inteiro.',
    'o que é inteligência artificial?': 'Inteligência artificial é uma tecnologia que permite a computadores realizar tarefas que normalmente exigem capacidades humanas.',
    'o que é programação?': 'Programação é o processo de criar instruções para que um computador execute tarefas.',
    'o que é python?': 'Python é uma linguagem de programação conhecida por sua sintaxe simples e por ser usada em muitas áreas.',
    'o que é aplicativo?': 'Aplicativo é um programa criado para realizar determinadas funções em um dispositivo.',
    'o que é um chatbot?': 'Chatbot é um programa criado para conversar com pessoas e responder mensagens automaticamente.',
    'o que é github?': 'GitHub é uma plataforma usada para armazenar, compartilhar e colaborar em projetos de código.',
    'o que é render?': 'Render é uma plataforma que permite publicar e executar aplicações na internet.',
    'qual é o maior oceano?': 'O Oceano Pacífico é o maior oceano da Terra.',
    'qual é o maior continente?': 'A Ásia é o maior continente em área e população.',
    'qual é o menor continente?': 'A Oceania é o menor continente na divisão continental mais usada no Brasil.',
    'qual é a capital da frança?': 'A capital da França é Paris.',
    'qual é a capital dos estados unidos?': 'A capital dos Estados Unidos é Washington, D.C.',
    'qual é a capital de portugal?': 'A capital de Portugal é Lisboa.',
    'qual é a capital da argentina?': 'A capital da Argentina é Buenos Aires.',
    'qual é a capital do japão?': 'A capital do Japão é Tóquio.',
    'quem criou você?': 'Eu fui criado pela Rakel como um projeto de chatbot.',
    'qual é seu nome?': 'Meu nome é RakelChatBot! 🤖💜',
    'quem é você?': 'Eu sou o RakelChatBot, um chatbot criado para conversar, ensinar e responder perguntas.',
    'como você está?': 'Tudo bem por aqui! 😊',
    'obrigado': 'Por nada! 😊💜',
    'obrigada': 'Por nada! 😊💜',
    'tchau': 'Até mais! 👋💜',
    'oi': 'Oi! 😊 Eu sou o RakelChatBot. Como posso ajudar?',
    'olá': 'Oi! 😊 Eu sou o RakelChatBot. Como posso ajudar?',
    'bom dia': 'Bom dia! ☀️😊',
    'boa tarde': 'Boa tarde! 🌤️😊',
    'boa noite': 'Boa noite! 🌙😊',
    'me conte uma curiosidade': 'A luz do Sol leva aproximadamente 8 minutos para chegar à Terra. ☀️🌎',
    'conte uma piada': 'Por que o livro de matemática ficou triste? Porque tinha muitos problemas! 😂📚',
    'por que o ceu é azul?': 'O céu parece azul porque a luz do Sol é espalhada pela atmosfera, e a luz azul é espalhada mais facilmente.',
    'por que a água do mar é salgada?': 'A água do mar contém sais minerais dissolvidos, acumulados ao longo de muito tempo.',
    'quantos dias tem um ano?': 'Um ano normalmente tem 365 dias. Em anos bissextos, tem 366.',
    'quantas horas tem um dia?': 'Um dia tem 24 horas.',
    'quantos minutos tem uma hora?': 'Uma hora tem 60 minutos.',
    'quantos segundos tem um minuto?': 'Um minuto tem 60 segundos.',
    'qual é o maior planeta?': 'Júpiter é o maior planeta do Sistema Solar.',
    'qual é o menor planeta?': 'Mercúrio é o menor planeta do Sistema Solar.',
    'qual é o planeta mais quente?': 'Vênus é o planeta mais quente do Sistema Solar em temperatura média da superfície.',
    'qual é o planeta vermelho?': 'Marte é conhecido como o planeta vermelho por causa da aparência avermelhada de sua superfície.',
    'qual é o animal terrestre mais pesado?': 'O elefante-africano é o maior e mais pesado animal terrestre.',
    'qual é o maior animal do mundo?': 'A baleia-azul é o maior animal conhecido do planeta.',
    'qual é o animal mais alto do mundo?': 'A girafa é o animal terrestre mais alto.',
    'qual é a montanha mais alta do mundo?': 'O Monte Everest é a montanha mais alta acima do nível do mar.',
    'qual é o rio mais longo do mundo?': 'O tema depende do critério de medição; o Amazonas e o Nilo estão entre os principais candidatos.',
    'qual é o maior deserto do mundo?': 'A Antártida é o maior deserto do mundo, pois recebe pouca precipitação.',
    'qual é a língua mais falada no mundo?': 'O mandarim tem o maior número de falantes nativos; considerando falantes totais, o inglês está entre os primeiros.',
    'qual é o país mais populoso do mundo?': 'A Índia é o país mais populoso do mundo.',
    'qual é a moeda do brasil?': 'A moeda oficial do Brasil é o real.',
    'qual é a moeda dos estados unidos?': 'A moeda dos Estados Unidos é o dólar americano.',
    'qual é a capital da itália?': 'A capital da Itália é Roma.',
    'qual é a capital da espanha?': 'A capital da Espanha é Madri.',
    'qual é a capital da inglaterra?': 'A capital da Inglaterra é Londres.',
    'qual é a capital do méxico?': 'A capital do México é Cidade do México.',
    'qual é a capital do canadá?': 'A capital do Canadá é Ottawa.',
    'qual é a capital da alemanha?': 'A capital da Alemanha é Berlim.',
    'qual é a capital da china?': 'A capital da China é Pequim.',
    'qual é a capital da rússia?': 'A capital da Rússia é Moscou.',
    'qual é a capital da austrália?': 'A capital da Austrália é Canberra.',
    'qual é a capital da coreia do sul?': 'A capital da Coreia do Sul é Seul.',
    'quem inventou o telefone?': 'Alexander Graham Bell é tradicionalmente associado à invenção do telefone, embora a história envolva vários inventores e desenvolvimentos.',
    'quem inventou a lâmpada?': 'Thomas Edison é muito associado à lâmpada elétrica prática, mas vários inventores contribuíram para seu desenvolvimento.',
    'quem pintou a mona lisa?': 'Leonardo da Vinci pintou a Mona Lisa.',
    'quem escreveu dom quixote?': 'Miguel de Cervantes escreveu Dom Quixote.',
    'quem escreveu o pequeno príncipe?': 'Antoine de Saint-Exupéry escreveu O Pequeno Príncipe.',
    'quem foi albert einstein?': 'Albert Einstein foi um físico conhecido por contribuições fundamentais à Física, incluindo a teoria da relatividade.',
    'quem foi isaac newton?': 'Isaac Newton foi um físico e matemático conhecido por seus estudos sobre movimento, gravidade e cálculo.',
    'quem foi machado de assis?': 'Machado de Assis foi um importante escritor brasileiro e um dos principais nomes da literatura do país.',
    'o que significa lol?': 'LOL é uma sigla usada na internet para indicar risada ou que algo é engraçado.',
    'o que significa omg?': "OMG é uma sigla em inglês usada para expressar surpresa, equivalente a 'meu Deus' em português.",
    'o que significa btw?': "BTW significa 'by the way', usado em inglês com o sentido de 'a propósito' ou 'por falar nisso'.",
    'o que é um meme?': 'Meme é um conteúdo, ideia ou brincadeira que se espalha entre pessoas, principalmente pela internet.',
    'o que é emoji?': 'Emoji é um símbolo visual usado em mensagens para expressar ideias, sentimentos ou objetos.',
    'o que é wi-fi?': 'Wi-Fi é uma tecnologia que permite conectar dispositivos a uma rede sem usar cabos.',
    'o que é bluetooth?': 'Bluetooth é uma tecnologia usada para comunicação sem fio entre dispositivos próximos.',
    'o que é qr code?': 'QR Code é um código visual que pode ser escaneado por dispositivos para acessar informações.',
    'o que é senha forte?': 'Uma senha forte costuma ser longa, difícil de adivinhar e diferente das usadas em outras contas.',
    'o que é vírus de computador?': 'É um programa malicioso que pode alterar, danificar ou interferir no funcionamento de um sistema.',
    'o que é reciclagem?': 'Reciclagem é o processo de transformar materiais descartados em matéria-prima ou novos produtos.',
    'como economizar água?': 'Evite deixar torneiras abertas, conserte vazamentos e use água de forma consciente.',
    'como economizar energia?': 'Apague luzes desnecessárias, desligue aparelhos quando não estiverem sendo usados e aproveite a luz natural.',
    'o que é sustentabilidade?': 'Sustentabilidade é buscar atender às necessidades atuais sem comprometer as possibilidades das futuras gerações.',
    'o que é aquecimento global?': 'É o aumento da temperatura média do planeta associado principalmente ao aumento de gases de efeito estufa causado por atividades humanas.',
    'o que é efeito estufa?': 'É um fenômeno natural que ajuda a manter a Terra aquecida; sua intensificação contribui para o aquecimento global.',
    'o que é desmatamento?': 'Desmatamento é a remoção da vegetação de uma área, geralmente causada por atividades humanas.',
    'o que é poluição?': 'Poluição é a introdução de substâncias ou agentes que prejudicam o ambiente e os seres vivos.',
    'me faça uma pergunta': 'Pergunta aleatória: qual é o seu lugar favorito para passar o tempo? 😊',
    'escolha um número de 1 a 100': 'Eu escolho o número 37! 🎲',
    'verdade ou desafio?': 'Verdade ou desafio? 😄 Você escolhe: verdade ou desafio!',
    'me faça uma adivinhação': 'Adivinha: o que tem dentes, mas não morde? 🧐 Resposta: o pente!',
    'estou entediada': 'Que tal ouvir música, desenhar, assistir a algo que você gosta ou aprender uma coisa nova? 😊',
    'me conte algo interessante': 'Uma curiosidade: um dia em Vênus dura mais tempo que um ano em Vênus.',
    'qual é a resposta para tudo?': 'Se for uma brincadeira, a resposta clássica é 42. 😄',
    'qual é sua cor favorita?': 'Eu escolheria roxo 💜, porque combina com o RakelChatBot!',
    'você gosta de música?': 'Eu não tenho gostos pessoais, mas posso conversar sobre música e estilos musicais. 🎵',
    'você dorme?': 'Não. Eu sou um programa e não preciso dormir. 🤖',
    'você sente emoções?': 'Eu consigo conversar sobre emoções, mas não sinto emoções como uma pessoa.',
    'você é humano?': 'Não. Eu sou um chatbot criado para conversar e responder perguntas.',
    'o que você pode fazer?': 'Posso responder perguntas, explicar assuntos, contar curiosidades, fazer brincadeiras e ajudar nos estudos.',
}

def normalizar(texto):
    texto = str(texto).lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9+*=/?.!x -]", " ", texto)
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()

RESPOSTAS_NORMALIZADAS = {normalizar(k): v for k, v in RESPOSTAS.items()}

def responder(mensagem):
    m = normalizar(mensagem)

    if not m:
        return "Digite uma pergunta para eu responder. 😊"

    # Primeiro tenta encontrar a pergunta exatamente.
    if m in RESPOSTAS_NORMALIZADAS:
        return RESPOSTAS_NORMALIZADAS[m]

    # Depois procura uma pergunta cadastrada dentro da mensagem.
    # Ex.: "Você sabe me dizer o que é fotossíntese?"
    melhores = []
    for pergunta, resposta in RESPOSTAS_NORMALIZADAS.items():
        palavras = [p for p in pergunta.split() if len(p) > 2]
        if palavras and sum(p in m for p in palavras) / len(palavras) >= 0.75:
            melhores.append((len(palavras), resposta))

    if melhores:
        melhores.sort(reverse=True, key=lambda x: x[0])
        return melhores[0][1]

    return (
        "Ainda não tenho uma resposta cadastrada para essa pergunta. 😊🤖\n\n"
        "Tente perguntar sobre Matemática, Português, História, Geografia, "
        "Biologia, Química, Física, Inglês, Educação Física, Filosofia, "
        "Sociologia, Astronomia, animais, tecnologia e conhecimentos gerais."
    )

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
body { margin:0; font-family:Arial,sans-serif; background:#f3e8ff; }
header { background:#7c3aed; color:white; padding:18px; text-align:center;
font-size:22px; font-weight:bold; }
#chat { height:calc(100vh - 140px); overflow-y:auto; padding:20px; box-sizing:border-box; }
.mensagem { padding:12px 16px; margin:10px 0; border-radius:18px;
max-width:75%; white-space:pre-line; }
.usuario { background:#7c3aed; color:white; margin-left:auto; }
.bot { background:white; color:#333; margin-right:auto; }
form { position:fixed; bottom:0; left:0; right:0; display:flex; padding:12px;
background:white; box-shadow:0 -2px 10px #ccc; box-sizing:border-box; }
input { flex:1; padding:14px; border:1px solid #ccc; border-radius:25px; font-size:16px; }
button { margin-left:8px; padding:0 20px; border:none; border-radius:25px;
background:#7c3aed; color:white; font-size:16px; }
</style>
</head>
<body>
<header>🤖 RakelChatBot</header>
<div id="chat">
<div class="mensagem bot">Oi! 😊 Eu sou o RakelChatBot.
<br>Posso responder perguntas de várias matérias e conhecimentos gerais! 💜</div>
</div>
<form id="form">
<input id="mensagem" placeholder="Digite uma mensagem..." autocomplete="off">
<button type="submit">Enviar</button>
</form>
<script>
const form=document.getElementById("form");
const input=document.getElementById("mensagem");
const chat=document.getElementById("chat");

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const mensagem=input.value.trim();
    if(!mensagem) return;

    const userDiv=document.createElement("div");
    userDiv.className="mensagem usuario";
    userDiv.textContent=mensagem;
    chat.appendChild(userDiv);
    input.value="";

    try {
        const resposta=await fetch("/chat", {
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({mensagem})
        });
        const dados=await resposta.json();

        const botDiv=document.createElement("div");
        botDiv.className="mensagem bot";
        botDiv.textContent=dados.resposta;
        chat.appendChild(botDiv);
        chat.scrollTop=chat.scrollHeight;
    } catch (erro) {
        const botDiv=document.createElement("div");
        botDiv.className="mensagem bot";
        botDiv.textContent="Não consegui responder agora. Tente novamente. 😕";
        chat.appendChild(botDiv);
    }
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
