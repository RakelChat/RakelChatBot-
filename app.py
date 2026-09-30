print("🤖 RakelChatBot iniciado!")

while True:
    mensagem = input("Você: ")

    if mensagem.lower() in ["oi", "olá", "ola"]:
        print("RakelChatBot: Oi! 😊 Como posso ajudar?")
    elif mensagem.lower() == "tchau":
        print("RakelChatBot: Até mais! 👋")
        break
    else:
        print("RakelChatBot: Ainda estou aprendendo. 🤖")
