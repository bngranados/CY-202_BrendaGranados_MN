
# Examen Parcial 1 | CY-202

# Brenda Nazaret Granados Ramírez

# 21 de Octubre 2026 | Semana 7

# Implemente un programa en Python para gestionar el inventario y analizar las ventas de una tienda. 

# Requerimientos: 

# El usuario indicará cuántos productos desea registrar.
# Por cada producto se solicitará:
## Código(único)
## Nombre del producto
## Precio unitario
## Cantidad en inventario
## Categoría (por ejemplo: "Electrónica", "Ropa", "Alimentos")

# Estructura de datos
## Los productos se almacenaran en un diccionario, donde la clave sera el codigo del producto y el valor otro diccionario con sus detalles

productos = {}

## Las ventas se almacenan en una lista de tuplas con la forma: (codigo, cantidad vendida, total de la venta)

ventas = []


# Validaciones
## Evitar codigos duplicados
## Validar que el precio y la cantidad sean valores numericos positivos
## Rechazar cualquier entrada invalida y volver a solicitarla

# Pedir un numero entero positivo

def pedir_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Error: el valor debe ser mayor que cero!")
        except ValueError:
            print("Error: ingrese solo numeros enteros!")

# Pedir un numero decimal positivo [para el precio]

def pedir_decimal_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("Error: el valor debe ser mayor que cero!")
        except ValueError:
            print("Error: ingrese solo numeros decimales!")

# Ingreso de datos
## Recibe el diccionario para poder registrar mas productos sin borrar los anteriores

def registrar_productos(productos):
    cantidad_productos = pedir_entero_positivo("Ingrese la cantidad de productos a registrar: ")

    for i in range(cantidad_productos):
        print(f"\nRegistro del producto {i + 1}:")

        ### Se utilizó 'while' para volver a solicitar el codigo si esta vacio o repetido
        
        while True:
            codigo = input("Codigo del producto: ").upper()
            if codigo == "":
                print("Error: el codigo no puede estar vacio!")
            elif codigo in productos:
                print("Error: ya existe un producto con ese codigo!")
            else:
                break

        nombre = input("Nombre del producto: ")
        precio = pedir_decimal_positivo("Precio unitario: ")
        cantidad = pedir_entero_positivo("Cantidad en inventario: ")
        categoria = input("Categoria: ")

        productos[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad, "categoria": categoria}
        print("El producto fue registrado correctamente.")

# Funcionalidades (usar funciones separadas)

# a) Mostrar todos los productos registrados
## (codigo, nombre, categoria, cantidad y precio total)

def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos registrados!")
    else:
        print("Productos registrados:")
        for codigo, datos in productos.items():
            precio_total = datos["precio"] * datos["cantidad"]
            print(f"- {codigo} | {datos['nombre']} | {datos['categoria']} | Cantidad: {datos['cantidad']} | Precio total: {precio_total:.2f}")

# b) Calcular el valor total del inventario
## Sumando el precio x cantidad de cada producto

def calcular_valor_inventario(productos):
    total = 0
    for codigo, datos in productos.items():
        total += datos["precio"] * datos["cantidad"]
    return total

# c) Permitir registrar ventas
## Indicando: codigo del producto y la cantidad vendida
## Actualizar la cantidad disponible en inventario
## Registrar cada venta en una lista de tuplas con la forma: ventas = [("P001", 3, 64500), ("P002", 2, 25000)]

def registrar_venta(productos, ventas):
    if len(productos) == 0:
        print("No hay productos registrados!")
    else:
        codigo = input("Codigo del producto a vender: ").upper()

        ### Validaciones: el producto debe existir y tener inventario
        
        if codigo not in productos:
            print("Error: el producto no existe!")
        elif productos[codigo]["cantidad"] == 0:
            print("Error: el producto no tiene inventario disponible!")
        else:
            disponible = productos[codigo]["cantidad"]
            cantidad = pedir_entero_positivo("Cantidad vendida: ")

            ### Validacion: no se puede vender mas de lo disponible
            
            if cantidad > disponible:
                print(f"Error: solo hay {disponible} unidades disponibles!")
            else:
                
                ### Se actualiza el inventario y se guarda la venta como tupla (codigo, cantidad, total)
                
                total_venta = productos[codigo]["precio"] * cantidad
                productos[codigo]["cantidad"] = disponible - cantidad
                ventas.append((codigo, cantidad, total_venta))
                print("La venta fue registrada correctamente.")

# d) Calcular
## El producto mas vendido (por unidades vendidas)

def producto_mas_vendido(productos, ventas):
    if len(ventas) == 0:
        print("Aun no hay ventas registradas!")
    else:
        totales = {}
        for venta in ventas:
            codigo = venta[0]
            cantidad = venta[1]
            if codigo in totales:
                totales[codigo] = totales[codigo] + cantidad
            else:
                totales[codigo] = cantidad

        mayor_total = max(totales.values())
        for codigo, total in totales.items():
            if total == mayor_total:
                print(f"Producto mas vendido: {codigo} - {productos[codigo]['nombre']} ({total} unidades vendidas)")

## El total de ingresos por ventas

def calcular_ingresos(ventas):
    total = 0
    for venta in ventas:
        total += venta[2]
    return total

## El promedio de ventas por categoria (promedio del monto de cada venta de la categoria)

def promedio_por_categoria(productos, ventas):
    if len(ventas) == 0:
        print("Aun no hay ventas registradas!")
    else:
        categorias = {}
        for venta in ventas:
            categoria = productos[venta[0]]["categoria"]
            if categoria in categorias:
                categorias[categoria].append(venta[2])
            else:
                categorias[categoria] = [venta[2]]

        print("Promedio de ventas por categoria: ")
        for categoria, totales in categorias.items():
            promedio = sum(totales) / len(totales)
            print(f"- {categoria}: {promedio:.2f}")


# e) Mostrar un resumen general con:
## Total de productos activos (los que aun tienen inventario)
## Valor restante del inventario
## Ingreso total generado por ventas

def mostrar_resumen(productos, ventas):
    activos = 0
    for codigo, datos in productos.items():
        if datos["cantidad"] > 0:
            activos += 1

    print("Resumen general:")
    print("Total de productos activos:", activos)
    print(f"Valor restante del inventario: {calcular_valor_inventario(productos):.2f}")
    print(f"Ingreso total generado por ventas: {calcular_ingresos(ventas):.2f}")


# Recomendacio
# Guardar el inventario actualizado y las ventas en un archivo de texto

def guardar_datos(productos, ventas):
    with open("inventario_de_ventas.txt", "w", encoding="utf-8") as archivo:
        archivo.write("INVENTARIO ACTUALIZADO\n")
        for codigo, datos in productos.items():
            archivo.write(f"{codigo} | {datos['nombre']} | {datos['categoria']} | Cantidad: {datos['cantidad']} | Precio: {datos['precio']:.2f}\n")

        archivo.write("\n VENTAS REGISTRADAS \n")
        for venta in ventas:
            archivo.write(f"Codigo: {venta[0]} | Cantidad: {venta[1]} | Total: {venta[2]:.2f}\n")

    print("Datos guardados en inventario_de_ventas.txt")

# Menu
## Opciones para registrar los productos, realizar las ventas y mostrar los reportes

print(" ¡Bienvenido al sistema de inventario y ventas! ")

while True:
    print("\n Tienda - Inventario y ventas ")
    print(" 1. Registrar productos ")
    print(" 2. Mostrar productos ")
    print(" 3. Valor total del inventario ")
    print(" 4. Registrar venta ")
    print(" 5. Producto mas vendido ")
    print(" 6. Total de ingresos por ventas ")
    print(" 7. Promedio de ventas por categoria ")
    print(" 8. Resumen general ")
    print(" 9. Salir ")
    opcion = input(" Por favor, elija una opcion: ")

    if opcion == "1":
        registrar_productos(productos)
    elif opcion == "2":
        mostrar_productos(productos)
    elif opcion == "3":
        print(f"Valor total del inventario: {calcular_valor_inventario(productos):.2f}")
    elif opcion == "4":
        registrar_venta(productos, ventas)
    elif opcion == "5":
        producto_mas_vendido(productos, ventas)
    elif opcion == "6":
        print(f"Total de ingresos por ventas: {calcular_ingresos(ventas):.2f}")
    elif opcion == "7":
        promedio_por_categoria(productos, ventas)
    elif opcion == "8":
        mostrar_resumen(productos, ventas)
    elif opcion == "9":
        guardar_datos(productos, ventas)
        print("Gracias por usar el sistema. \n ¡Hasta luego! ")
        break
    else:
        print("Opcion invalida!")   
           