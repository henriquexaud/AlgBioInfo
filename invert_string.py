def inverter_palavras(string):
    # Divide a string em palavras
    palavras = string.split()

    # Inverte cada palavra
    palavras_invertidas = [palavra[::-1] for palavra in palavras]

    # Junta as palavras invertidas em uma string
    string_invertida = ' '.join(palavras_invertidas)
    return string_invertida

# Leitura da string
string_entrada = input("Digite uma string: ")

# Chama a função para inverter as palavras
string_invertida = inverter_palavras(string_entrada)
print("String com palavras invertidas:", string_invertida)

