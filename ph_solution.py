def responder_pergunta(resposta):
    if resposta.lower() == 's':
        return "OK, continuando..."
    elif resposta.lower() == 'n':
        return "OK, parando..."
    else:
        return "Resposta inválida. Por favor, digite 's' para continuar ou 'n' para parar."

# Inicializa a resposta com um valor que não 'n' ou 'N'
resposta_usuario = 's'

# Loop enquanto a resposta for diferente de 'n' ou 'N'
while resposta_usuario.lower() != 'n':
    resposta_usuario = input("Continuar (s/n)? ")
    mensagem = responder_pergunta(resposta_usuario)
    print(mensagem)
