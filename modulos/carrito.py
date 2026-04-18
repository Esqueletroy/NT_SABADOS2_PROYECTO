carrito = []

def agregar_producto(producto):
    carrito.append(producto)
    return "Producto agregado al carrito"

def ver_carrito():
    return carrito
