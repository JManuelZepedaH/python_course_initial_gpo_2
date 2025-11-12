import time
#Decoradores -> Aumentar funcionalidad sin modificar la funcion original

def decorador(func):
    def envoltura():
        print("Inicio")
        func()
        print("fin")
    return envoltura

@decorador
def saludar():
    print("Hola Mundo")
    
saludar()

#Decorador con arg y kwards
def decorador(func):
    def envoltura(*args, **kwargs):
        print(f"Iniico con args {args} y kwards {kwargs}")
        func(*args, **kwargs)
        print("fin")
    return envoltura

@decorador
def suma(n1: int, n2:int) -> None:
    print(f"La suma es: {n1 +n2}")

suma(5,7)
#----------------------------------------------------------------

def decorador2(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        ejecucion = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecucion: {fin - inicio}")
        return ejecucion
    return envoltura

@decorador2
def enchular():
    time.sleep(1)
    return "finalizado"

print(enchular())