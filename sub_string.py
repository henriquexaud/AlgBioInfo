def substituir_caracteres(string_original, string_substituir, string_substituta):
    # Substitui os caracteres da segunda string pelos da terceira na primeira string
    nova_string = string_original.replace(string_substituir, string_substituta)
    return nova_string

# Leitura das strings
string_original = input("1a string: ")
string_substituir = input("2a string: ")
string_substituta = input("3a string: ")

# Substitui os caracteres e imprime o resultado
resultado_substituicao = substituir_caracteres(string_original, string_substituir, string_substituta)
print("Resultado da substituição:", resultado_substituicao)