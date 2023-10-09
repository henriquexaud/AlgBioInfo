def contar_caracteres(string):
    contagem = {}  # Dicionário para armazenar a contagem de caracteres

    # Percorre cada caractere na string
    for char in string:
        # Incrementa a contagem para o caractere atual ou inicializa com 1 se for a primeira ocorrência
        contagem[char] = contagem.get(char, 0) + 1

    # Imprime o resultado no formato desejado
    for char, count in contagem.items():
        print(f"{char}: {count}x")

# Leitura da string
string = input("String: ")

# Chama a função para contar e imprimir a contagem de caracteres
contar_caracteres(string)
