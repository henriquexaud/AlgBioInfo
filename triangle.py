def imprimir_triangulo(altura):
    for i in range(altura):
        for j in range(i + 1):
            print("*", end="")
        print()

# Leitura da altura do triângulo
altura = int(input("Digite a altura do triângulo: "))

# Chamada da função para imprimir o triângulo
imprimir_triangulo(altura)
