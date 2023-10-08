R1 = float(input("Digite o valor da resistência R1: "))
R2 = float(input("Digite o valor da resistência R2: "))
R3 = float(input("Digite o valor da resistência R3: "))

R = 1 / ( (1/R1) + (1/R2) + (1/R3) )

print(f"A resistência combinada é: {R:.2f} ohms")