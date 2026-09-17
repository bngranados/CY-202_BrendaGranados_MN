# Utilizar listas y condicionales

# Crear una lista de productos
productos = ["Leche", "Pan", "Huevos", "Frijoles Molidos", "Mantequilla"]

# Mostrar menu

# Agregar productos a la lista
while True:
    print("\nMenu:")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        producto = input("Nombre del producto: ")
        productos.append(producto)
    elif opcion == "2":
        for p in productos:
            print(p)
    elif opcion == "3":
        buscado = input("Producto a buscar: ")
        if buscado in productos:
            print("Producto encontrado")
        else:
            print("Producto no encontrado")
    elif opcion == "4":
        break
    else:
        print("Opcion invalida")