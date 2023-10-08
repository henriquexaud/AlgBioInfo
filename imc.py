altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
nome = input("Digite seu nome: ")

imc = peso / (altura * altura)

print(f"{nome}, com {altura}m de altura e pesando {peso}kg, seu IMC é: {imc:.2f}.")