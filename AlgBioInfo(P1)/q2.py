def segundo_menor_maior(lista_numeros):
    if len(lista_numeros) < 2:
        return None, None
    
    lista_ordenada = sorted(set(lista_numeros))

    return lista_ordenada[1], lista_ordenada[-2]

numeros = input("Digite os números separados por espaço: ").split()
segundo_menor, segundo_maior = segundo_menor_maior(numeros)

print("Segundo menor valor:", segundo_menor)
print("Segundo maior valor:", segundo_maior)