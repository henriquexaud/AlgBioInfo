def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Leitura do número até o qual queremos encontrar números primos
limite_superior = int(input("Digite o número até o qual deseja encontrar números primos: "))

print(f"Números primos até {limite_superior}:")
for i in range(1, limite_superior + 1):
    if eh_primo(i):
        print(i, end=" ")
