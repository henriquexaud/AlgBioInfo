salario = float(input("Digite o valor do salário: "))
porcentagem = float(input("Digite a porcentagem de aumento: "))

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

print(f"O valor do aumento é: {aumento:.2f}")
print(f"O novo salário é: {novo_salario:.2f}")