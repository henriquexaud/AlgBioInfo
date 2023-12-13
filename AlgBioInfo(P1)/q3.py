def calcular_alpha(n):
    b_n = (1 - 1/n)**n
    b_n_1 = (1 - 1/(n-1))**(n-1)
    return abs(b_n - b_n_1)

def calcular_e_aproximado(alpha):
    n = 2
    erro = calcular_alpha(n)

    while erro > alpha:
        n += 1
        erro = calcular_alpha(n)

    valor_aproximado_e = (1 - 1/n)**n
    return round(valor_aproximado_e, 4), n

alpha = 0.001
valor_e_aproximado, n_aproximacao = calcular_e_aproximado(alpha)
print(f"Valor aproximado de e: {valor_e_aproximado} (com erro < {alpha})")
print(f"Necessário {n_aproximacao} iterações para atingir o erro menor que {alpha}")
