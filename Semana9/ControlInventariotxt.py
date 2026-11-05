# Ejercicio Integrador: Control de Inventario con Archivo TXT
 
# Apertura de archivos en Python
## open() es la funcion que permite abrir un archivo: archivo = open("datos.txt", "modo")
## El modo indica para que se abre el archivo:
## "r" = leer archivo
## "w" = escribir desde cero
## "a" = agregar informacion (no elimina el contenido del archivo)
## "x" = crear archivo nuevo
## En este ejercicio se usa "w" para guardar el inventario y "r" para leerlo
 
 
# Solicitar el nombre del producto, precio y cantidad disponible
## Se guardan en el archivo inventario.txt
## Se abre con el modo "w": escribe el archivo desde cero
cantidad_productos = int(input("Cuantos productos desea registrar? "))
 
archivo = open("inventario.txt", "w")
 
for i in range(cantidad_productos):
    print(f"\nProducto {i + 1}:")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad disponible: "))
 
    ## Cada producto se guarda en una linea, con los datos separados por comas
    archivo.write(nombre + "," + str(precio) + "," + str(cantidad) + "\n")
 
## close() guarda los cambios
archivo.close()
 
 
# Leer la informacion almacenada en el archivo
## Se abre con el modo "r": leer archivo
## try / except evita que el programa se cierre si el archivo no existe
productos = []
 
try:
    archivo = open("inventario.txt", "r")
 
    for linea in archivo:
        # strip elimina los saltos de linea \n
        # split separa los datos por comas
        # append agrega el dato a la lista
        productos.append(linea.strip().split(","))
 
    archivo.close()
except FileNotFoundError:
    print("Archivo no existe")
 
 
# Reporte del inventario actual
## Muestra cada producto con su precio y cantidad disponible
print("\nReporte de inventario:")
 
valor_total = 0
 
for producto in productos:
    nombre = producto[0]
    precio = float(producto[1])
    cantidad = int(producto[2])
    print(f"- {nombre} | Precio: {precio} | Cantidad: {cantidad}")
 
    ## El valor del inventario suma precio x cantidad de cada producto
    valor_total += precio * cantidad
 
 
# Cantidad total de productos diferentes y valor total del inventario
print("\nCantidad total de productos diferentes:", len(productos))
print(f"Valor total del inventario: {valor_total:.2f}")
 