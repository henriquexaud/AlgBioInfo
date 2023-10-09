list_even = []
list_odd = []
list_numbers = []

for i in range(20):
    n = int(input("Digite um número: "))
    list_numbers.append(n)
    if n % 2 == 0:
        list_even.append(n)
    else:
        list_odd.append(n)

print("Numeros pares: ", list_even)
print("Numeros impar: ", list_odd)
print("Lista completa: ", list_numbers)