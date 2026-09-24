# Objetivo: Utilizar tuplas y funciones.

def mostrar_estudiantes(lista):
    for nombre in lista:
        print(nombre)

def contar_estudiantes(lista):
    return len(lista)

estudiantes = []
cantidad = int(input("Cuantos estudiantes desea ingresar? "))

for i in range(cantidad):
    nombre = input("Nombre del estudiante: ")
    estudiantes.append(nombre)

mostrar_estudiantes(estudiantes)
print("Cantidad de estudiantes:", contar_estudiantes(estudiantes))