# Práctica Integradora

# Brenda Nazaret Granados Ramírez

# Sistema de Gestión de Estudiantes

# Desarrollar un programa que permita registrar estudiantes y sus calificaciones utilizando los conceptos aprendidos hasta el momento:
# Variables, Condicionales, Ciclos (for y/o while), Funciones, Listas, Tuplas, Diccionarios, Parámetros y retorno de valores.


# 6. Uso de Tuplas
# La información debe mostrarse al inicio del programa, pasé esto al inicio como el pdf lo pide al inicio
curso = ("Programación Intermedia", "CY202", 4)
print("Nombre del curso:", curso[0])
print("Código:", curso[1])
print("Cantidad de semanas:", curso[2])


# 1. Registro de Estudiantes

estudiantes = {}
cantidad = int(input("Cuantos estudiantes desea ingresar? "))

for i in range(cantidad):
    nombre = input("Nombre del estudiante: ")
    nota = float(input(f"Nota de {nombre}: "))
    
# Reto Adicional (Opcional)
# Validar que las notas estén entre 0 y 100. Si el usuario ingresa una nota inválida, deberá solicitarla nuevamente.

    while nota < 0 or nota > 100:
        print("Nota inválida. Debe estar entre 0 y 100.")
        nota = float(input(f"Nota de {nombre}: "))
    estudiantes[nombre] = nota
    
# 2. Función para Mostrar Estudiantes
def mostrar_estudiantes(lista):
    print("Lista de estudiantes:")
    for nombre, nota in lista.items():
        print("- ", nombre, ":", nota)
        
# 3. Función para Calcular el Promedio

def calcular_promedio(lista):
    total = sum(lista.values())
    promedio = total / len(lista)
    return promedio

# 4. Función para Obtener la Mejor Nota
def mejor_nota(lista):
    mejor = max(lista.values())
    return mejor

#5. Función para Buscar Estudiantes
def buscar_estudiante(lista):
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in lista:
        print(f"Estudiante encontrado: {nombre} con nota {lista[nombre]}")
    else:
        print("Estudiante no encontrado")

# 7. Estadísticas Generales
if len(estudiantes) > 0:
    mostrar_estudiantes(estudiantes)
    buscar_estudiante(estudiantes)

    print("\nEstadísticas Generales:")
    print(f"Cantidad de estudiantes: {len(estudiantes)}")
    print(f"Promedio del grupo: {calcular_promedio(estudiantes):.2f}")
    print(f"Nota más alta: {mejor_nota(estudiantes)}")
    print(f"Nota más baja: {min(estudiantes.values())}")
else:
    print("No se registraron estudiantes.")
    
