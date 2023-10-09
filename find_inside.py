def encontrar_posicao_substring(string_principal, substring):
    posicao = string_principal.find(substring)
    return posicao

# Leitura das strings
string_principal = input("1a string: ")
substring = input("2a string: ")

# Verifica se a substring ocorre dentro da string principal
posicao_inicio = encontrar_posicao_substring(string_principal, substring)

# Imprime a posição de início, se encontrado
if posicao_inicio != -1:
    print("A segunda string ocorre na posição de início:", posicao_inicio)
else:
    print("A segunda string não ocorre dentro da primeira.")
