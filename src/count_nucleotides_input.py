'''
    ¿Cuantas A, C, G y T hay en la secuencia dada por el usuario?
'''

dna = input('Dame una secuencia de DNA:\n')

print(f"Frecuencia de nucleotidos\n {dna}\n A:{dna.count('A')} C:{dna.count('C')} G:{dna.count('G')} T:{dna.count('T')}")