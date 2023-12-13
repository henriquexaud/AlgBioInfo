import math

def calcular_seno_hiperbolico(x):
    seno_hiperbolico = 0

    for n in range(20):
        termo_n = ((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)
        seno_hiperbolico += termo_n

    return seno_hiperbolico

x = float(input("Digite o valor de x: "))
seno_hiperbolico_valor = calcular_seno_hiperbolico(x)
print(f"O seno hiperbólico de {x} é aproximadamente: {seno_hiperbolico_valor}")