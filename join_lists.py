def gerar_terceira_lista(lista1, lista2):
    terceira_lista = lista1 + lista2
    return terceira_lista

# Leitura das duas listas
lista1 = input("Digite os elementos da primeira lista separados por espaço: ").split()
lista2 = input("Digite os elementos da segunda lista separados por espaço: ").split()

# Convertendo os elementos para inteiros
lista1 = [int(x) for x in lista1]
lista2 = [int(x) for x in lista2]

# Chama a função para gerar a terceira lista
terceira_lista = gerar_terceira_lista(lista1, lista2)

# Imprime a terceira lista
print("Terceira lista (concatenação da primeira e segunda lista):", terceira_lista)
