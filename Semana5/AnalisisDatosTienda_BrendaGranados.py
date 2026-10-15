# Práctica Integradora

# Brenda Nazaret Granados Ramírez

# Ejercicio 2 - Analisis de datos en una tienda

# Simular un sistema de ventas de una tienda:
# Usar un diccionario donde las claves sean los productos y los valores sean listas con el precio y cantidad vendida.
# Calcula el total de ingresos de la tienda.
# Muestra el producto más vendido.


# producto: [precio, cantidad vendida]
ventas = {
    "Camisa": [8000, 15],
    "Pantalon": [15000, 10],
    "Zapatos": [25000, 6],
    "Gorra": [5000, 22]
}

# Total de ingresos
total_ingresos = 0
for producto, datos in ventas.items():
    precio = datos[0]
    cantidad = datos[1]
    total_ingresos += precio * cantidad

print(f"Total de ingresos: {total_ingresos}")

# Producto mas vendido (por cantidad de unidades)
mas_vendido = ""
mayor_cantidad = 0
for producto, datos in ventas.items():
    if datos[1] > mayor_cantidad:
        mayor_cantidad = datos[1]
        mas_vendido = producto

print(f"Producto mas vendido: {mas_vendido} ({mayor_cantidad} unidades)")
