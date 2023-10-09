import time

def contagem_regressiva():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)  # Aguarda 1 segundo antes de imprimir o próximo número

    print("Fogo!")

# Chama a função para iniciar a contagem regressiva
contagem_regressiva()
