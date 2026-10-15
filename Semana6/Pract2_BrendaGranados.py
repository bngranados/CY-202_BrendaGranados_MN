# Sistema de Matricula de Cursos

# Brenda Nazaret Granados Ramirez

# Enunciado:
## Desarrollar una aplicacion que administre cursos y matriculas de estudiantes utilizando listas, diccionarios, tuplas, ciclos, condicionales y funciones

# Ingreso de datos:
## El programa debe solicitar la informacion requerida por teclado y almacenarla en las estructuras definidas


# Estructuras de datos

# Diccionario principal de cursos:
## La clave es el codigo del curso y el valor es otro diccionario (interno) con nombre, carrera y cupos.
cursos = {}

# Lista de tuplas para registrar las matriculas.
# Cada tupla guarda: (codigo del curso, nombre del estudiante)
matriculas = []


# Funcion auxiliar: pedir un numero entero mayor que cero
## Usa try/except para manejar el error si el usuario escribe texto (ValueError)
def pedir_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Error: el valor debe ser mayor que cero.")
        except ValueError:
            print("Error: ingrese solo numeros enteros.")


# Registrar cursos
## Solicita codigo, nombre, carrera y cupos, y los guarda en el diccionario. | Validaciones: codigo unico y cupos mayores que cero
def registrar_curso(cursos):
    codigo = input("Codigo del curso (ejemplo CUR101): ").upper()

    ### Validacion: el codigo no puede estar vacio
    if codigo == "":
        print("Error: el codigo no puede estar vacio.")
        return

    ### Validacion: el codigo debe ser unico
    if codigo in cursos:
        print("Error: ya existe un curso con ese codigo.")
        return

    nombre = input("Nombre del curso: ")
    carrera = input("Carrera: ")

    ### Validacion: los cupos deben ser mayores que cero
    cupos = pedir_entero_positivo("Cupos disponibles: ")

    ### Se guarda el diccionario interno dentro del diccionario principal
    cursos[codigo] = {"nombre": nombre, "carrera": carrera, "cupos": cupos}
    print("Curso registrado correctamente.")


# Mostrar cursos registrados
## Recorre el diccionario con .items() y muestra los datos de cada curso
def mostrar_cursos(cursos):
    if len(cursos) == 0:
        print("No hay cursos registrados.")
        return

    print("Cursos registrados:")
    for codigo, datos in cursos.items():
        print(f"- {codigo} | {datos['nombre']} | {datos['carrera']} | Cupos disponibles: {datos['cupos']}")


# Registrar matricula
## Validaciones: el curso debe existir y no se puede matricular si no hay cupos. | Al matricular se descuenta un cupo y se guarda una tupla en la lista
def registrar_matricula(cursos, matriculas):
    if len(cursos) == 0:
        print("No hay cursos registrados.")
        return

    codigo = input("Codigo del curso a matricular: ").upper()

    ### Validacion: el curso debe existir
    if codigo not in cursos:
        print("Error: el curso no existe.")
        return

    ### Validacion: no se permite matricular cuando no existan cupos
    if cursos[codigo]["cupos"] == 0:
        print("Error: no hay cupos disponibles en este curso.")
        return

    estudiante = input("Nombre del estudiante: ")

    ### Validacion: el nombre no puede estar vacio
    if estudiante == "":
        print("Error: el nombre no puede estar vacio.")
        return

    ### Se descuenta un cupo y se registra la matricula como tupla
    cursos[codigo]["cupos"] = cursos[codigo]["cupos"] - 1
    matriculas.append((codigo, estudiante))
    print("Matricula registrada correctamente.")


# Calcular total de matriculas
## Muestra cuantas matriculas se hicieron en total
def total_matriculas(matriculas):
    print("Total de matriculas realizadas:", len(matriculas))


# Determinar curso con mas matriculas
## Acumula las matriculas por codigo en un diccionario y luego busca el mayor total con max()
def curso_mas_matriculado(cursos, matriculas):
    if len(matriculas) == 0:
        print("Aun no hay matriculas registradas.")
        return

    totales = {}
    for matricula in matriculas:
        codigo = matricula[0]
        if codigo in totales:
            totales[codigo] = totales[codigo] + 1
        else:
            totales[codigo] = 1

    mayor_total = max(totales.values())
    for codigo, total in totales.items():
        if total == mayor_total:
            print(f"Curso con mas matriculas: {codigo} - {cursos[codigo]['nombre']} ({total} matriculas)")


# Mostrar historial de matriculas
## Recorre la lista de tuplas y muestra cada matricula en orden
def mostrar_historial(matriculas):
    if len(matriculas) == 0:
        print("Aun no hay matriculas registradas.")
        return

    print("Historial de matriculas:")
    numero = 1
    for matricula in matriculas:
        print(f"{numero}. Curso: {matricula[0]} | Estudiante: {matricula[1]}")
        numero += 1


# Calcular promedio por carrera
## Agrupa los cupos disponibles por carrera en un diccionario de listas y calcula el promedio de cupos por curso en cada carrera
def promedio_por_carrera(cursos):
    if len(cursos) == 0:
        print("No hay cursos registrados.")
        return

    carreras = {}
    for codigo, datos in cursos.items():
        carrera = datos["carrera"]
        if carrera in carreras:
            carreras[carrera].append(datos["cupos"])
        else:
            carreras[carrera] = [datos["cupos"]]

    print("Promedio de cupos disponibles por carrera:")
    for carrera, cupos in carreras.items():
        promedio = sum(cupos) / len(cupos)
        print(f"- {carrera}: {promedio:.1f}")


# Menu para acceder a cada funcionalidad mediante funciones independientes
while True:
    print("\nSistema de matricula de cursos")
    print("1. Registrar curso")
    print("2. Mostrar cursos")
    print("3. Registrar matricula")
    print("4. Total de matriculas")
    print("5. Curso con mas matriculas")
    print("6. Historial de matriculas")
    print("7. Promedio de cupos por carrera")
    print("8. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        registrar_curso(cursos)
    elif opcion == "2":
        mostrar_cursos(cursos)
    elif opcion == "3":
        registrar_matricula(cursos, matriculas)
    elif opcion == "4":
        total_matriculas(matriculas)
    elif opcion == "5":
        curso_mas_matriculado(cursos, matriculas)
    elif opcion == "6":
        mostrar_historial(matriculas)
    elif opcion == "7":
        promedio_por_carrera(cursos)
    elif opcion == "8":
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")