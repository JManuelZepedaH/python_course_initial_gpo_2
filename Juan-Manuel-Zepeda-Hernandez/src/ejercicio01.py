# Comentario en linera

'''
Comentarios 
multi
linea
'''

# Tipos de datos
entero = 10
print(type(entero))

flotante =10.5
print(type(flotante))

cadena = "Hola, Mudo"
print(type(cadena))

booleana = True
print(type(booleana))


#Estructuras de datos
# ListaS
lista: list = [1,2,3]
print(type(lista))

# Tupla
tupla: tuple = (1,2,3)
print(type(tupla))
# No se puede actualizar la tupla
# tupla[2] = 4
# print(tupla)
#----

# Diccionarios
diccionario: dict = {"clave1":"valor1"}

# Sets
mi_set:set = {1,2,3}

# F-strings
nombre: str = "Juan"

# Compresiones
cuadrados:list = [x**2 for x in range(10)]
print(cuadrados)

