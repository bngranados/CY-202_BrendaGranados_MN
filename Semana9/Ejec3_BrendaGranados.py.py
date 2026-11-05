# Ejercicio Integrador: Sistema de Control de Agenda Personal

# Brenda Nazaret Granados Ramírez

# Desarrollar un programa que administre una agenda personal usando archivos de texto.

archivo = "agenda.txt"

print("=== REGISTRO DE CONTACTOS ===")

# Registrar los contactos con nombre completo, numero de telefono y correo electronico
try:
    cantidad_contactos = int(input("¿Cuántos contactos desea registrar?: "))

    ## Modo "a" para mantener la informacion aunque el programa finalice
    with open(archivo, "a", encoding="utf-8") as f:

        for i in range(cantidad_contactos):
            print(f"\nContacto #{i + 1}")

            nombre = input("Nombre completo: ").strip()
            telefono = input("Número de teléfono: ").strip()
            correo = input("Correo electrónico: ").strip()

            ### Guardar el contacto en el archivo, separado por comas
            f.write(f"{nombre},{telefono},{correo}\n")

    print("\nContactos registrados correctamente.")

except ValueError:
    print("Error: la cantidad de contactos debe ser un número entero.")

except Exception as e:
    print("Ocurrió un error:", e)


# Leer el archivo y recuperar cada contacto en una lista
contactos = []

try:
    with open(archivo, "r", encoding="utf-8") as f:

        for linea in f:
            ### strip() elimina salto de linea | split(",") separa los datos | append() agrega el contacto a la lista
            datos = linea.strip().split(",")
            contactos.append(datos)

except FileNotFoundError:
    print("No se encontró el archivo agenda.txt")

except Exception as e:
    print("Error al leer el archivo:", e)


# Reporte con todos los contactos registrados
print("\n=== REPORTE DE AGENDA ===")

if len(contactos) == 0:
    print("No hay contactos registrados.")
else:
    for contacto in contactos:
        print(f"Nombre   : {contacto[0]}")
        print(f"Teléfono : {contacto[1]}")
        print(f"Correo   : {contacto[2]}")
        print("-" * 30)

    print(f"Total de contactos registrados: {len(contactos)}")