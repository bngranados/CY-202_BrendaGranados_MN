# Conversion a Mayusculas usando upper ()

# Crear una lista vacia
nombres = []

# Solicitar 5 nombres y guardarlos
for i in range(5):
    nombre = input("Nombre: ")
    nombres.append(nombre)

# Mostrar los nombres en mayusculas usando upper()
for nombre in nombres:
    print(nombre.upper())