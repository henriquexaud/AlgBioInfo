from Bio import SeqIO

def comparar_sequencias(seq_a, seq_b, limite=200):
    diferenças = 0
    posições_diferentes = []

    for i in range(min(len(seq_a), len(seq_b), limite)):
        if seq_a[i] != seq_b[i]:
            diferenças += 1
            posições_diferentes.append(i + 1)

    return diferenças, posições_diferentes

arquivo_a = "Seq_a.fasta"
arquivo_b = "Seq_b.fasta"

with open(arquivo_a, "r") as handle_a, open(arquivo_b, "r") as handle_b:
    sequencia_a = next(SeqIO.parse(handle_a, "fasta")).seq
    sequencia_b = next(SeqIO.parse(handle_b, "fasta")).seq

diferencas, posicoes_diferentes = comparar_sequencias(sequencia_a, sequencia_b, limite=200)

print(f"Número de nucleotídeos diferentes nas primeiras 200 posições: {diferencas}")
print(f"Posições diferentes: {posicoes_diferentes}")
