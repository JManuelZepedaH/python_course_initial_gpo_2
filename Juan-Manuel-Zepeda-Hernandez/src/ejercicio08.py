# Herencia y composicion

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Hace sonido")


class Perro(Animal):
    def __init__(self, nombre="Perro"):
        super().__init__("Perro")
        
    def hablar(self):
        print(self.nombre)
        print("Guau guau")
        
perro = Perro()

perro.hablar()  # Output: Guau guau
        