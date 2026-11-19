# Ejercicio Programado #2: Sistema de Gestión de Estudiantes y Calificaciones

# Brenda Nazaret Granados Ramírez

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas
    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    def __str__(self):
        return f"{self.nombre} | Edad: {self.edad} | Promedio: {self.calcular_promedio():.2f}"


# Clase GestorEstudiantes: maneja el archivo de almacenamiento
class GestorEstudiantes:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    # Guardar un estudiante en el archivo con el formato: nombre,edad,nota1;nota2;nota3
    ## Modo "a" para agregar al final sin borrar lo anterior
    def agregar_estudiante(self, estudiante):
        notas_texto = []
        for nota in estudiante.notas:
            notas_texto.append(str(nota))

        with open(self.nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{estudiante.nombre},{estudiante.edad},{';'.join(notas_texto)}\n")

    # Leer el archivo y devolver una lista de objetos Estudiante
    ## Modo "r" para leer | strip() quita el salto de línea | split() separa los datos
    def leer_estudiantes(self):
        estudiantes = []

        try:
            with open(self.nombre_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")

                    nombre = datos[0]
                    edad = int(datos[1])

                    notas = []
                    for nota in datos[2].split(";"):
                        notas.append(float(nota))

                    estudiantes.append(Estudiante(nombre, edad, notas))
        except FileNotFoundError:
            pass

        return estudiantes

    # Buscar un estudiante por nombre y devolver el objeto si existe
    def buscar_estudiante(self, nombre):
        for estudiante in self.leer_estudiantes():
            if estudiante.nombre.lower() == nombre.lower():
                return estudiante
        return None


# Solicitar el nombre del estudiante (no vacío y solo letras)
def solicitar_nombre():
    while True:
        nombre = input("Nombre del estudiante: ").strip()
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
        elif not nombre.replace(" ", "").isalpha():
            print("Error: el nombre debe contener solo letras.")
        else:
            return nombre


# Solicitar la edad (entero entre 1 y 120)
def solicitar_edad():
    while True:
        try:
            edad = int(input("Edad: "))
            if edad >= 1 and edad <= 120:
                return edad
            print("Error: la edad debe estar entre 1 y 120.")
        except ValueError:
            print("Error: ingrese solo números enteros.")


# Solicitar la cantidad de notas a registrar (entero mayor que cero)
def solicitar_cantidad_notas():
    while True:
        try:
            cantidad = int(input("Cantidad de notas a registrar: "))
            if cantidad > 0:
                return cantidad
            print("Error: la cantidad debe ser mayor que cero.")
        except ValueError:
            print("Error: ingrese solo números enteros.")


# Solicitar una calificación entre 0 y 100
def solicitar_nota(numero_nota):
    while True:
        try:
            nota = float(input(f"Nota #{numero_nota}: "))
            if nota >= 0 and nota <= 100:
                return nota
            print("Error: la nota debe estar entre 0 y 100.")
        except ValueError:
            print("Error: ingrese solo números.")


# Solicitar las calificaciones y devolver una lista de decimales
def solicitar_notas():
    cantidad = solicitar_cantidad_notas()
    notas = []

    for i in range(cantidad):
        notas.append(solicitar_nota(i + 1))

    return notas


# Registrar un estudiante: solicita los datos, crea el objeto y lo guarda en el archivo
def registrar_estudiante(gestor):
    nombre = solicitar_nombre()
    edad = solicitar_edad()
    notas = solicitar_notas()

    estudiante = Estudiante(nombre, edad, notas)
    gestor.agregar_estudiante(estudiante)
    print("Estudiante registrado correctamente.")


# Mostrar todos los estudiantes registrados con sus notas y promedios
def mostrar_estudiantes(gestor):
    estudiantes = gestor.leer_estudiantes()

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("\n=== ESTUDIANTES REGISTRADOS ===")
        for estudiante in estudiantes:
            print(estudiante)
            print(f"Notas: {estudiante.notas}")
            print("-" * 30)


# Buscar un estudiante por nombre y mostrar su información
def buscar_estudiante_por_nombre(gestor):
    nombre = solicitar_nombre()
    estudiante = gestor.buscar_estudiante(nombre)

    if estudiante is None:
        print("Estudiante no encontrado.")
    else:
        print("\nEstudiante encontrado:")
        print(estudiante)
        print(f"Notas: {estudiante.notas}")


# Mostrar las opciones del sistema
def mostrar_menu():
    print("\n=== SISTEMA DE ESTUDIANTES Y CALIFICACIONES ===")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por nombre")
    print("4. Salir")


# Controlar la ejecución del programa y las opciones del menú
def main():
    gestor = GestorEstudiantes("estudiantes.txt")

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar_estudiante(gestor)
        elif opcion == "2":
            mostrar_estudiantes(gestor)
        elif opcion == "3":
            buscar_estudiante_por_nombre(gestor)
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida")


main()