# Buscar nombre 

# Lista con 5 nombres
Nombres = ["Ignacio", "Raquel", "Emily", "Lizeth", "GianLuca"]

# Solicitar nombre al usuario

nombre = input("Ingrese un nombre: ")

# Verificar si el nombre se encuentra en la lista
if nombre in Nombres:
    print("Nombre encontrado")
else:
    print("Nombre no encontrado")