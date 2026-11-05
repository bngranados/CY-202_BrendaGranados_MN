# Ejercicio Integrador: Sistema de Registro de Pasajeros de Aerolínea

# Brenda Nazaret Granados Ramírez

# Desarrollar un programa para la aerolínea FideAir que 
# registre los pasajeros de sus vuelos usando archivos de texto.

# Importante: 
# Apertura de archivos en Python
## open() es la función que permite abrir un archivo: open("archivo.txt", "modo")
## Modos:
### "r" = leer el archivo
### "w" = escribir desde cero (borra lo anterior)
### "a" = agregar informacion al final (no borra lo anterior)
### "x" = crear un archivo nuevo
## write() escribe en el archivo | read() lo lee | close() lo cierra para guardar cambios
## with open(...) as archivo: cierra el archivo automaticamente, no requiere close()

archivo = "pasajeros.txt"

print("=== REGISTRO DE PASAJEROS FIDEAIR ===")

# Solicitar la cantidad de pasajeros y sus datos: nombre completo, numero de pasaporte y destino
try:
    cantidad_pasajeros = int(input("¿Cuántos pasajeros desea registrar?: "))

    ## Modo "a" para conservar la informacion para futuras consultas
    with open(archivo, "a", encoding="utf-8") as f:

        for i in range(cantidad_pasajeros):
            print(f"\nPasajero #{i + 1}")

            nombre = input("Nombre completo: ").strip()
            pasaporte = input("Número de pasaporte: ").strip()
            destino = input("Destino del vuelo: ").strip()

            ### Guardar el registro en el archivo
            f.write(f"{nombre},{pasaporte},{destino}\n")

    print("\nPasajeros registrados correctamente.")

except ValueError:
    print("Error: la cantidad de pasajeros debe ser un número entero.")

except Exception as e:
    print("Ocurrió un error:", e)


# Leer los registros del archivo y recuperarlos en una lista
pasajeros = []

try:
    with open(archivo, "r", encoding="utf-8") as f:

        for linea in f:
            ### strip() elimina el salto de linea | split(",") separa los datos | append() agrega el pasajero a la lista
            datos = linea.strip().split(",")
            pasajeros.append(datos)

except FileNotFoundError:
    print("No se encontró el archivo pasajeros.txt")

except Exception as e:
    print("Error al leer el archivo:", e)


# Reporte con todos los pasajeros registrados
print("\n=== REPORTE DE PASAJEROS ===")

if len(pasajeros) == 0:
    print("No hay pasajeros registrados.")
else:
    for pasajero in pasajeros:
        print(f"Nombre    : {pasajero[0]}")
        print(f"Pasaporte : {pasajero[1]}")
        print(f"Destino   : {pasajero[2]}")
        print("-" * 30)

    print(f"Total de pasajeros registrados: {len(pasajeros)}")