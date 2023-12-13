import math

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def termo_seno(x, n):
    return (-1)**n * x**(2*n + 1) / fatorial(2*n + 1)

def termo_cosseno(x, n):
    return (-1)**n * x**(2*n) / fatorial(2*n)

def soma_infinita_seno(x, n):
    if n == 0:
        return termo_seno(x, n)
    else:
        return termo_seno(x, n) + soma_infinita_seno(x, n - 1)

def soma_infinita_cosseno(x, n):
    if n == 0:
        return termo_cosseno(x, n)
    else:
        return termo_cosseno(x, n) + soma_infinita_cosseno(x, n - 1)

def seno(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    return soma_infinita_seno(angulo_radianos, 30)

def cosseno(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    return soma_infinita_cosseno(angulo_radianos, 30)

def tangente(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    return seno(angulo_graus) / cosseno(angulo_graus)

angulo = float(input("Digite o ângulo em graus: "))

print(f"Seno: {seno(angulo)}")
print(f"Cosseno: {cosseno(angulo)}")
print(f"Tangente: {tangente(angulo)}")


