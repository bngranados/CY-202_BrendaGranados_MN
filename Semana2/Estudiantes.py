# Crear lista de estudiantes

# Crear una lista vacia
estudiantes = []

# Solicitar 3 nombres y guardarlos en la lista
for i in range(3):
    nombre = input("Nombre del estudiante: ")
    estudiantes.append(nombre)

# Mostar los nombres de los estudiantes
for nombre in estudiantes:
    print(nombre)