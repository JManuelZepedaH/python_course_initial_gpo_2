#Inyeccion de dependecias

# Inyeccion por constructor
from abc import ABC, abstractmethod


class ServiceEmail:
    def send_email(self,mensaje):
        print(f"Enviando correo: {mensaje}")

class Notificador:
    def __init__(self, servicice: ServiceEmail):
        self.servicice = servicice
    
    def notificar(self, mensaje):
        self.servicice.send_email(mensaje)

service_email = ServiceEmail()
notifica = Notificador(servicice=service_email)

notifica.notificar("Este es un mensaje importante por Constructor")
#-----------------------------------------------------------

# Inyeccion por setter
class ServiceEmail:
    def send_email(self,mensaje):
        print(f"Enviando correo: {mensaje}")

class Notificador:
    def __init__(self, service_email: ServiceEmail):
        self.servicice = service_email
        
    def notificar(self, mensaje):
        self.servicice.send_email(mensaje)

service_email = ServiceEmail()
# notifica = Notificador(servicice=service_email)
#-----------------------------------------------------------

class MotorBase(ABC):
    @abstractmethod
    def encender(self):
        pass

class MotorElectrico(MotorBase):
    def encender(self):
        print("Encendiendo electrico")
        
class Auto:
    def __init__(self, motor_base:MotorBase):
        self.motor = motor_base
    
    def arrancar(self):
        self.motor.encender()

auto =Auto(MotorElectrico())
auto.arrancar()