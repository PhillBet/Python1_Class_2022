'''
    Abriendo y Leyendo archivos con Python
'''

# Nombre del archivo con su path
my_file_name = 'data/dna.txt'

# Abrir el archivo como objeto
my_file = open(my_file_name, 'r')
print(my_file)

# Leer el contenido del archivo
my_file_content = my_file.read().rstrip('\n')

# Mostrar el contenido del archivo
print(my_file_content)

data_length = len(my_file_content)

print(f"La longitud de la secuencia {my_file_content} es: {data_length}")

# Cerrar el archivo
my_file.close()
print(my_file.read())