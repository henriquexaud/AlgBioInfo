def caracteres_comuns(string1, string2):
    # Inicializa uma lista para armazenar os caracteres comuns
    caracteres_comuns = []

    # Percorre cada caractere na primeira string
    for char in string1:
        # Verifica se o caractere está presente na segunda string
        if char in string2 and char not in caracteres_comuns:
            caracteres_comuns.append(char)

    # Cria a terceira string com os caracteres comuns
    terceira_string = ''.join(caracteres_comuns)
    return terceira_string

# Leitura das strings
string1 = input("1a string: ")
string2 = input("2a string: ")

# Gera a terceira string com os caracteres comuns
terceira_string = caracteres_comuns(string1, string2)

# Imprime a terceira string
print("/033[31mTerceira string com caracteres comuns:", terceira_string)
