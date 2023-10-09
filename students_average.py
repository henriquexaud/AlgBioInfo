num_alunos = 5
num_notas = 4

# Inicialize as listas para armazenar as notas
notas_alunos = [[] for _ in range(num_alunos)]

# Leitura das notas
for aluno in range(num_alunos):
    print(f"Notas do aluno {aluno + 1}: ")
    for i in range(num_notas):
        nota_valida = False
        while not nota_valida:
            nota_str = input(f"Digite a nota {i + 1} para o aluno {aluno + 1}: ")
            if nota_str.lower() == 'q':
                break
            elif nota_str.replace('.', '', 1).lstrip('-').isdigit():
                nota = float(nota_str)
                if 0 <= nota <= 10:
                    notas_alunos[aluno].append(nota)
                    nota_valida = True
                else:
                    print("Por favor, digite uma nota entre 0 e 10.")
            else:
                print("Por favor, digite uma nota válida.")

# Calcular média de cada aluno
medias_alunos = [sum(notas) / len(notas) for notas in notas_alunos]

# Calcular a média da turma
media_turma = sum(medias_alunos) / num_alunos

# Contar alunos com média maior que 6
alunos_aprovados = sum(1 for media in medias_alunos if media > 6)

# Imprimir as médias e a quantidade de alunos aprovados
for aluno in range(num_alunos):
    print(f"Média do aluno {aluno + 1}: {medias_alunos[aluno]:.2f}")

print(f"Média da turma: {media_turma:.2f}")
print(f"Quantidade de alunos aprovados: {alunos_aprovados}")
