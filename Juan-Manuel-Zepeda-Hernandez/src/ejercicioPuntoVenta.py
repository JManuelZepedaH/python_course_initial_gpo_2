Productos: dict = {"zote":15,"cloro":20,"foca":25}
productos2:list = [15,20,25]
print(Productos.get("cloro"))
iva:float = 0.16

def calculoPrecio(producto:list,iva) -> list:
    precioFinalProductos:list = list(map(lambda a: a * (1 + iva), producto))
    return precioFinalProductos

print(calculoPrecio(productos2,iva))