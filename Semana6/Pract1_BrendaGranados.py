# Sistema de Biblioteca Universitaria

# Brenda Nazaret Granados Ramírez

# Enunciado:
## Desarrollar una aplicación que administre libros y préstamos utilizando listas, diccionarios, tuplas, ciclos, condicionales y funciones

# Ingreso de datos: 
## El programa debe solicitar la información requerida por teclado y almacenarla en las estructuras definidas


# Estructuras de datos
 
# Diccionario principal de libros:
## La clave es el codigo del libro y el valor es otro diccionario (interno) con titulo, categoria y cantidad.
libros = {}
 
# Lista de tuplas para registrar los prestamos.
# Cada tupla guarda: (codigo del libro, cantidad prestada)
prestamos = []
 
 
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
 
 
# Registrar libros
## Solicita codigo, titulo, categoria y cantidad, y los guarda en el diccionario. | Validaciones: codigo unico y cantidad mayor que cero
def registrar_libro(libros):
    codigo = input("Codigo del libro (ejemplo LIB001): ").upper()
 
    ### Validacion: el codigo no puede estar vacio
    if codigo == "":
        print("Error: el codigo no puede estar vacio.")
        return
 
    ### Validacion: el codigo debe ser unico
    if codigo in libros:
        print("Error: ya existe un libro con ese codigo.")
        return
 
    titulo = input("Titulo: ")
    categoria = input("Categoria: ")
 
    ### Validacion: la cantidad debe ser mayor que cero
    cantidad = pedir_entero_positivo("Cantidad de ejemplares: ")
 
    ### Se guarda el diccionario interno dentro del diccionario principal
    libros[codigo] = {"titulo": titulo, "categoria": categoria, "cantidad": cantidad}
    print("Libro registrado correctamente.")
 
 
# Mostrar libros registrados
## Recorre el diccionario con .items() y muestra los datos de cada libro
def mostrar_libros(libros):
    if len(libros) == 0:
        print("No hay libros registrados.")
        return
 
    print("Libros registrados:")
    for codigo, datos in libros.items():
        print(f"- {codigo} | {datos['titulo']} | {datos['categoria']} | Disponibles: {datos['cantidad']}")
 
 
# Registrar prestamo
## Validaciones: el libro debe existir y no se puede prestar mas de lo disponible. | Al prestar se descuenta de la cantidad disponible y se guarda una tupla en la lista
def registrar_prestamo(libros, prestamos):
    if len(libros) == 0:
        print("No hay libros registrados.")
        return
 
    codigo = input("Codigo del libro a prestar: ").upper()
 
    ### Validacion: el libro debe existir
    if codigo not in libros:
        print("Error: el libro no existe.")
        return
 
    disponible = libros[codigo]["cantidad"]
    cantidad = pedir_entero_positivo("Cantidad a prestar: ")
 
    ### Validacion: no se puede prestar mas de la existencia disponible
    if cantidad > disponible:
        print(f"Error: solo hay {disponible} ejemplares disponibles.")
        return
 
    ### Se descuenta de la existencia y se registra el prestamo como tupla
    libros[codigo]["cantidad"] = disponible - cantidad
    prestamos.append((codigo, cantidad))
    print("Prestamo registrado correctamente.")
 
 
# Calcular total de prestamos
## Muestra cuantos prestamos se hicieron y el total de unidades prestadas
def total_prestamos(prestamos):
    total_unidades = 0
    for prestamo in prestamos:
        total_unidades += prestamo[1]
 
    print("Cantidad de prestamos realizados:", len(prestamos))
    print("Total de unidades prestadas:", total_unidades)
 
 
# Determinar libro mas prestado
## Acumula las unidades prestadas por codigo en un diccionario y luego busca el mayor total con max()
def libro_mas_prestado(libros, prestamos):
    if len(prestamos) == 0:
        print("Aun no hay prestamos registrados.")
        return
 
    totales = {}
    for prestamo in prestamos:
        codigo = prestamo[0]
        cantidad = prestamo[1]
        if codigo in totales:
            totales[codigo] = totales[codigo] + cantidad
        else:
            totales[codigo] = cantidad
 
    mayor_total = max(totales.values())
    for codigo, total in totales.items():
        if total == mayor_total:
            print(f"Libro mas prestado: {codigo} - {libros[codigo]['titulo']} ({total} unidades prestadas)")
 
 
# Mostrar historial de prestamos
## Recorre la lista de tuplas y muestra cada prestamo en orden
def mostrar_historial(prestamos):
    if len(prestamos) == 0:
        print("Aun no hay prestamos registrados.")
        return
 
    print("Historial de prestamos:")
    numero = 1
    for prestamo in prestamos:
        print(f"{numero}. Codigo: {prestamo[0]} | Cantidad prestada: {prestamo[1]}")
        numero += 1
 
 
# Calcular promedio por categoria
## Agrupa las cantidades disponibles por categoria en un diccionario de listas y calcula el promedio de ejemplares por libro en cada categoria
def promedio_por_categoria(libros):
    if len(libros) == 0:
        print("No hay libros registrados.")
        return
 
    categorias = {}
    for codigo, datos in libros.items():
        categoria = datos["categoria"]
        if categoria in categorias:
            categorias[categoria].append(datos["cantidad"])
        else:
            categorias[categoria] = [datos["cantidad"]]
 
    print("Promedio de ejemplares por categoria:")
    for categoria, cantidades in categorias.items():
        promedio = sum(cantidades) / len(cantidades)
        print(f"- {categoria}: {promedio:.1f}")
 
 
# Menu para acceder a cada funcionalidad mediante funciones independientes
while True:
    print("\nBiblioteca universitaria")
    print("1. Registrar libro")
    print("2. Mostrar libros")
    print("3. Registrar prestamo")
    print("4. Total de prestamos")
    print("5. Libro mas prestado")
    print("6. Historial de prestamos")
    print("7. Promedio por categoria")
    print("8. Salir")
    opcion = input("Elija una opcion: ")
 
    if opcion == "1":
        registrar_libro(libros)
    elif opcion == "2":
        mostrar_libros(libros)
    elif opcion == "3":
        registrar_prestamo(libros, prestamos)
    elif opcion == "4":
        total_prestamos(prestamos)
    elif opcion == "5":
        libro_mas_prestado(libros, prestamos)
    elif opcion == "6":
        mostrar_historial(prestamos)
    elif opcion == "7":
        promedio_por_categoria(libros)
    elif opcion == "8":
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")





























































