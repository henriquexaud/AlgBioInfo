def palavras_mais_de_tres_caracteres(string):
    # Divide a string em palavras
    palavras = string.split()

    # Filtra apenas as palavras com mais de três caracteres
    palavras_mais_longas = [palavra for palavra in palavras if len(palavra) > 3]

    return palavras_mais_longas

# Leitura da string
string_entrada = input("Digite uma string: ")

# Chama a função para obter as palavras com mais de três caracteres
palavras_longas = palavras_mais_de_tres_caracteres(string_entrada)

# Imprime as palavras com mais de três caracteres, separadas por vírgula
print("Palavras com mais de três caracteres:", ", ".join(palavras_longas))
