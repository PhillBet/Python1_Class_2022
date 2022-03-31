'''
    ¿Cuál es el porcetaje de AT y GC en la secuencia del archivo 
    dna.txt = 'ACTGTACGTGCACTGATC'?
    Escribe un programa que te regrese el porcentaje de AT y GC
    pero que te pregunte la ruta y el nombre del archivo de DNA.
'''
# Pedir la ruta y la nombre del nombre del archivo de DNA
file_name = input('Dame la rutay nombre del archivo de DNA:\n')

# Abrir, leer, quitar saltos de linea y asignar a variable la secuencia
dna = open(file_name).read().strip()

# Mostrar mensaje
print(f"Archivo de secuencia: {file_name}\n Porcentaje de AT y GC:\n AT: {dna.count('AT')}\n GC: {dna.count('GC')}\n")