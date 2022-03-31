'''
    ENCABEZADO
'''
# Variables
saludo = "Buenos dias"
nombre = "Andrea"
mensaje = saludo + ' ' + nombre
mensaje += '!'

# Funcion de tamaño de un string
print(len(mensaje)) # Funcion

# Metodo de busqueda
print(mensaje.find('Andrea')) # Retorna: 0
print(mensaje.find('Kevin')) # Retorna: -1

# Metodos de cambio mayusculas o minusculas
print(mensaje.lower()) # mayusculas
print(mensaje.upper()) # minusculas

# Metodo de reemplazo de subcadena
print(mensaje.replace('dias', 'noches'))

# Strings como arreglos 
'''
'HELLO'
 01234
-54321
'''
arreglo_caracteres = 'HELLO'

# Tomar un caracter del string
print(arreglo_caracteres[1])
print(arreglo_caracteres[-3])

# Tomar una parte del String
print(arreglo_caracteres[1:4])

# Metodo para contar un substring en un string
print(arreglo_caracteres.count('L'))
