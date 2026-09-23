# Evaluación Práctica Integradora
# Brenda Nazaret Granados Ramírez

# Sistema de Registro y Control de Cursos


# Parte 1 – Informacion General del Curso
# Crear una tupla llamada curso que almacene: Nombre del curso, código y duración en semanas.

curso = ("Programacion Intermedia", "CY202", 6)
print("Curso:", curso[0])
print("Codigo:", curso[1])
print("Duracion:", curso[2])

# Parte 2 – Registro de Estudiantes
# El sistema deberá solicitar al usuario la cantidad de estudiantes que desea registrar.

estudiantes = []
num_estudiantes = int(input("Ingrese la cantidad de estudiantes a registrar: "))
for i in range(num_estudiantes):
    nombre = input("Nombre del estudiante: ")
    estudiantes.append(nombre)

print("Estudiantes registrados:")
for estudiante in estudiantes:
    print("- ", estudiante)
    
# Parte 3 – Registro de Notas
# El sistema deberá registrar UNA nota por cada estudiante, las notas deben almacenarse en otra lista independiente.

notas = []
for estudiante in estudiantes:
    nota = float(input(f"Ingrese la nota de {estudiante}:"))
    notas.append(nota)

# Parte 4 – Funciones Obligatorias
# Función 1 – Mostrar estudiantes: Crear una función que reciba la lista de estudiantes y muestre todos los nombres utilizando un ciclo.
def mostrar_estudiantes(lista_estudiantes):
    print("Lista de estudiantes:")
    for estudiante in lista_estudiantes:
        print("- ", estudiante)


# Función 2 – Calcular promedio
# Crear una función que: reciba la lista de notas, calcula el promedio, y retorna el resultado.
def calcular_promedio(lista_notas):
    total = sum(lista_notas)
    promedio = total / len(lista_notas)
    return promedio

# Función 3 – Validar estudiante
# Crear una función que: reciba la lista de estudiantes, solicite un nombre, valide si existe usando in, muestre “Estudiante encontrado” o “Estudiante no encontrado”
def validar_estudiante(lista_estudiantes):
    nombre = input("Ingrese un nombre para buscar: ")
    if nombre in lista_estudiantes:
        print("Estudiante encontrado")
    else:
        print("Estudiante no encontrado")


# Parte 5 – Estadísticas Generales
# El programa deberá mostrar: promedio general, nota más alta, nota más baja, cantidad total de estudiantes.
# Restricción: Las estadísticas deben calcularse utilizando funciones integradas de Python vistas en clase

print("Estadísticas Generales:")
print("Promedio general:", calcular_promedio(notas))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("Cantidad total de estudiantes:", len(estudiantes))

# Parte 6 – Ordenamiento
# El sistema deberá ordenar las notas de menor a mayor y mostrarlas.

orden_notas = sorted(notas)
print("Notas ordenadas de menor a mayor:", orden_notas)

# Parte 7 – Validación Académica
# Después de calcular el promedio general:  si el promedio es mayor o igual a 70: mostrar “Grupo aprobado” de lo contrario:mostrar “Grupo en riesgo académico”

if calcular_promedio(notas) >= 70:
    print("Grupo aprobado")
else:
    print("Grupo en riesgo académico") 
    
    


