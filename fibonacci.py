def sequencia_fibonacci(n):
    # Inicializa os primeiros dois termos
    fibonacci = [0, 1]

    # Gera a sequência de Fibonacci até o enésimo termo
    for i in range(2, n):
        proximo_termo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_termo)

    return fibonacci

# Leitura do valor de "n"
n = int(input("Digite o valor de n para a sequência de Fibonacci: "))

# Verifica se o valor de "n" é válido
if n < 1:
    print("Por favor, insira um número inteiro maior ou igual a 1.")
else:
    # Gera a sequência de Fibonacci até o enésimo termo
    fibonacci_sequence = sequencia_fibonacci(n)

    # Imprime a sequência de Fibonacci
    print("Sequência de Fibonacci até o", n, "º termo:")
    print(fibonacci_sequence)
