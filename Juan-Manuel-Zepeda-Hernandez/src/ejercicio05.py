class CustomError(Exception):
    #clase de error personalizada
    pass

def funcion_con_error(n1:int) -> None:
    if(n1 < 0):
        raise CustomError("Error: numero menor a cero")
    print("El numero es correcto")



# Try catch
try:
    funcion_con_error(-5)
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Ejecucion correcta")
finally:
    print("Ejecucion finalizada")