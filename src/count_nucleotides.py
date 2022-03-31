'''
    ¿Cuantas A, C, G y T hay en la secuencia?
    'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
'''

dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

total_A = dna.count('A')
print(f"Frecuencia de nucleotidos\n {str(dna)}\n A:{A} C:{dna.count('C')} G:{dna.count('G')} T:{dna.count('T')}")
print(f"texto {total_A}")