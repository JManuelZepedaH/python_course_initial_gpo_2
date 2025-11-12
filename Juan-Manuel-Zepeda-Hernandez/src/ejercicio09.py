#Modelado de objertos mediante composicion y herencia

class Motor:
    def __init__(self, tipo: str):
        self.tipo = tipo

class Rueda:
    def __init__(self, tamano: int):
        self.tamano = tamano

class Coche:
    def __init__(self, marca: str, motor: Motor, ruedas: list[Rueda]):
        self.marca = marca
        self.motor = motor
        self.ruedas = ruedas

auto_uno = Coche(
    marca="Toyota",
    motor=Motor(tipo="V6"),
    ruedas=[Rueda(tamano=16) for _ in range(4)]
)

auto_uno.desc