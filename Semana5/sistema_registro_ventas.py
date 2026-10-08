# Ejercicio Integrador - Sistema de registro de ventas

def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: ingrese solo numeros.")

ventas = {}

cantidad_productos = int(pedir_numero("Cuantos productos desea registrar? "))

for i in range(cantidad_productos):
    producto = input("Nombre del producto: ")
    cantidad_ventas = int(pedir_numero(f"Cuantas ventas desea registrar de {producto}? "))
    lista_ventas = []
    for j in range(cantidad_ventas):
        monto = pedir_numero(f"Monto de la venta #{j + 1}: ")
        lista_ventas.append(monto)
    ventas[producto] = lista_ventas

print("\nResumen de ventas:")
totales = {}
for producto, lista in ventas.items():
    total = sum(lista)
    try:
        promedio = total / len(lista)
    except ZeroDivisionError:
        promedio = 0
    totales[producto] = total
    print(f"{producto}: total = {total:.2f} | promedio = {promedio:.2f}")

if len(totales) > 0:
    mayor_total = max(totales.values())
    for producto, total in totales.items():
        if total == mayor_total:
            print(f"Producto con mayor venta total: {producto} ({mayor_total:.2f})")
else:
    print("No se registraron productos.")