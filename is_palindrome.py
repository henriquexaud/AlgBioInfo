def e_palindromo(frase):
    # Remove espaços e pontuações e converte para minúsculas
    frase = ''.join(c.lower() for c in frase if c.isalnum())

    # Verifica se a frase é igual à sua reversa
    return frase == frase[::-1]

# Exemplo de uso
frase = input("Digite uma frase: ")

if e_palindromo(frase):
    print(f"A frase '{frase}' é um palíndromo.")
else:
    print(f"A frase '{frase}' não é um palíndromo.")
