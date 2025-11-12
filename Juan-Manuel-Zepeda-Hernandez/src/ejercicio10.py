class Procesador:
    def __init__(self, marca: str, nucleo: int):
        self.marca = marca
        self.nucleo = nucleo

class Memoria:
    def __init__(self, tamano: int, velocidad: int):
        self.tamano = tamano
        self.velocidad = velocidad

class Computadora:
    def __init__(self, procesador: Procesador, memoria:Memoria):
        self.procesador = procesador
        self.memoria = memoria
    
    def descripcion(self):
        print("Procesador")
        print(f"Marca: {self.procesador.marca}")
        print(f"Nucleos: {self.procesador.nucleo}")
        print(f"Memoria")
        print(f"Tamano: {self.memoria.tamano}")
        print(f"Velocidad: {self.memoria.velocidad}")
        
producto_uno = Computadora(
    memoria=Memoria(tamano=16, velocidad=3200),
    procesador=Procesador(marca="Intel", nucleo=8)
)

producto_uno.descripcion()
