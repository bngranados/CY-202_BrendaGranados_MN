# Objetivo: Utilizar funciones y tuplas para almacenar información de productos.

def mostrar_producto(producto):
    print("Nombre:", producto[0])
    print("Precio:", producto[1])
    print("Categoria:", producto[2])

producto = ("Laptop", 500000, "Electronica")

mostrar_producto(producto)