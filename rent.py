km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias pelo qual o carro foi alugado: "))

custo_dias = dias_alugados * 60
custo_km = km_percorridos * 0.15

total_a_pagar = custo_dias + custo_km

print(f"O preço a pagar é: R$ {total_a_pagar:.2f}")