'''
    ¿Dónde empieza el codón inical AUG (TAC) en la secuencia 'AAGGTACGTCGCGCGTTATTAGCCTAAT'?
'''
dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'
codon = 'TAC'
print(f'El codon {codon} empieza en la posicion: {dna.find(codon)}')