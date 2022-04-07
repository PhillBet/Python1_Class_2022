'''
    Dada una secuencia de DNA en un archivo llamado sequence.txt 
    reverso de la secuencia e imprimirlo
'''

dna = input('Dame una secuencia de DNA:\n')

file_name = dna
file_content = open(file_name, 'r').read()

# print(file_content[::-1])
file_content.reverse()
print(file_content)
