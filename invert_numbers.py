def imprimir_lista_inversa(lista):
    # Imprime a lista na ordem inversa
    for i in range(len(lista) - 1, -1, -1):
        print(lista[i], end=" ")

# Leitura da lista de números
numeros = []
for i in range(10):
    numero = input(f"Digite o {i + 1}º número: ")
    numeros.append(numero)

# Chama a função para imprimir a lista na ordem inversa
print("Números na ordem inversa:")
imprimir_lista_inversa(numeros)
