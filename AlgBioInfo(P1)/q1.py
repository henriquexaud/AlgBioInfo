def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def avaliar_situacao_obesidade(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade"

pessoas = []

num_pessoas = int(input("Digite o número de pessoas: "))

for i in range(num_pessoas):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    sexo = input(f"Digite o sexo da pessoa {i+1} (M/F): ").upper()
    peso = float(input(f"Digite o peso da pessoa {i+1} (kg): "))
    altura = float(input(f"Digite a altura da pessoa {i+1} (m): "))

    imc = calcular_imc(peso, altura)
    situacao_obesidade = avaliar_situacao_obesidade(imc)

    pessoa = {
        'nome': nome,
        'sexo': sexo,
        'peso': peso,
        'altura': altura,
        'imc': imc,
        'situacao_obesidade': situacao_obesidade
    }

    pessoas.append(pessoa)

imc_total = sum(pessoa['imc'] for pessoa in pessoas)
imc_medio = imc_total / num_pessoas

situacoes_obesidade = {
    'Abaixo do peso': 0,
    'Peso normal': 0,
    'Sobrepeso': 0,
    'Obesidade': 0,
}

for pessoa in pessoas:
    situacao = pessoa['situacao_obesidade']
    situacoes_obesidade[situacao] += 1

print("Resumo:")
print(f"Quantidade de pessoas: {num_pessoas}")
print(f"IMC médio: {imc_medio:.2f}")

for situacao, quantidade in situacoes_obesidade.items():
    print(f"Quantidade de pessoas com {situacao}: {quantidade}")

