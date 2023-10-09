def calcular_estatisticas_temperatura(temperaturas):
    if not temperaturas:
        return None, None, None

    menor_temp = min(temperaturas)
    maior_temp = max(temperaturas)
    media_temp = sum(temperaturas) / len(temperaturas)

    return menor_temp, maior_temp, media_temp

# Leitura das temperaturas
temperaturas = []
print("Digite as temperaturas separadas por espaços (ex: -10 -8 0 1 2 5 -2 -4)")
temperaturas_str = input("Temperaturas: ")

# Dividindo as temperaturas com base nos espaços e processando
temperaturas_input = temperaturas_str.split()
for temperatura_str in temperaturas_input:
    if temperatura_str.lower() == 'q':
        break
    elif temperatura_str.replace('.', '', 1).lstrip('-').isdigit():
        temperatura = float(temperatura_str)
        temperaturas.append(temperatura)
    else:
        print("Entrada inválida. Por favor, insira um número ou 'q' para parar.")

# Chama a função para calcular as estatísticas das temperaturas
menor, maior, media = calcular_estatisticas_temperatura(temperaturas)

# Imprime as estatísticas
if menor is not None and maior is not None and media is not None:
    print("Menor temperatura:", menor)
    print("Maior temperatura:", maior)
    print("Temperatura média:", media)
else:
    print("Nenhuma temperatura foi inserida.")
