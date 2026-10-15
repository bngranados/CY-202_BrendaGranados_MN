# Práctica Integradora

# Brenda Nazaret Granados Ramírez


# Ejercicio 1 - Gestion de contactos

# Crear un programa que administre una agenda de contactos. El programa debe:

# Permitir agregar un contacto con nombre, teléfono y correo.
# Permitir buscar un contacto por nombre.
# Mostrar la lista completa de contactos.


def agregar_contacto(contactos):
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    correo = input("Correo: ")
    contactos[nombre] = (telefono, correo)
    print("Contacto agregado.")

def buscar_contacto(contactos):
    nombre = input("Nombre a buscar: ")
    if nombre in contactos:
        datos = contactos[nombre]
        print(f"Nombre: {nombre} | Telefono: {datos[0]} | Correo: {datos[1]}")
    else:
        print("Contacto no encontrado.")

def mostrar_contactos(contactos):
    if len(contactos) == 0:
        print("La agenda esta vacia.")
    else:
        print("Lista de contactos:")
        for nombre, datos in contactos.items():
            print(f"- {nombre} | Telefono: {datos[0]} | Correo: {datos[1]}")

contactos = {}

while True:
    print("\nAgenda de contactos")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        agregar_contacto(contactos)
    elif opcion == "2":
        buscar_contacto(contactos)
    elif opcion == "3":
        mostrar_contactos(contactos)
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")
        
        
