# Args y Kwargs

#Argumentos posicionales.
def procesar_datos(*args) -> None:
    print(f"Argumentos posicionales recibidos: {args}")

procesar_datos(2,3,4)

# kwargs: Argumentos nombrados
def saludos_dinamicos(**kwargs) -> None:
    print(f"Argumentos nombrados: {kwargs}")

saludos_dinamicos(nombre="Juan", edad=27)

# Generadores -> Para manejar grandes volúmenes de datos, utilizan yield en lugar de return
def generar_datos(limite:int):
    print("Inicio del generador")
    for num in range(limite):
        print(f"Bucle: {num}")
        yield num
    print("Fin")

def generar_datos_tradicional(limite:int):
    print("Inicio del generador")
    resultado = []
    for num in range(limite):
        print(f"Bucle: {num}")
        resultado.append(num)
    print("Fin")
    return resultado

print("Uso de generador")
generador = generar_datos(5)

for item in generador:
    print(f"Valor generado: {item}")
    
print("USo de la funcion tradicional")
