'''
Para crear una funcion se declara con la palabra "def"
'''

def saludar(nombre:str) -> str:
    return f"Hola {nombre} Bienvenido al curso"

print(saludar("Juan"))
#-----------------------------------------------------------

# Lambdas
sumar = lambda a,b: a + b
resultado:int = sumar(5,3)
print(f"El resultados de la suma es: {resultado}")

# Maps
print(list(map(lambda a: a**2, range(10))))

# Filters
print(list(filter(lambda x: x % 2 == 0, range(10))))