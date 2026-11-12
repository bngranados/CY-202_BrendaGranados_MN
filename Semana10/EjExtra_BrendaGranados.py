# Ejercicio Extra (Ejercicio 5): Sistema de biblioteca con herencia

# Brenda Nazaret Granados Ramírez

# Clase padre
class Persona:
    def __init__(self, nombre, identificacion):
        self._nombre = nombre
        self._identificacion = identificacion

    def obtener_nombre(self):
        return self._nombre

    def obtener_identificacion(self):
        return self._identificacion

    def mostrar_info(self):
        print(f"Persona: {self._nombre}, Identificación: {self._identificacion}")

    # Texto que se guarda en el archivo personas.txt
    def a_linea(self):
        return f"Persona,{self._nombre},{self._identificacion}"


# Clase hija Usuario
class Usuario(Persona):
    def __init__(self, nombre, identificacion):
        super().__init__(nombre, identificacion)
        self._historial_prestamos = []

    def agregar_prestamo(self, titulo):
        self._historial_prestamos.append(titulo)

    # Sobrescritura del método
    def mostrar_info(self):
        print(f"Usuario: {self._nombre}, Identificación: {self._identificacion}, Historial de préstamos: {self._historial_prestamos}")

    # Sobrescritura del método: los préstamos se separan con ;
    def a_linea(self):
        historial = ";".join(self._historial_prestamos)
        return f"Usuario,{self._nombre},{self._identificacion},{historial}"


# Clase hija Bibliotecario
class Bibliotecario(Persona):
    def __init__(self, nombre, identificacion, permiso_registrar):
        super().__init__(nombre, identificacion)
        self._permiso_registrar = permiso_registrar

    def puede_registrar(self):
        return self._permiso_registrar

    # Sobrescritura del método
    def mostrar_info(self):
        print(f"Bibliotecario: {self._nombre}, Identificación: {self._identificacion}, Permiso para registrar libros: {self._permiso_registrar}")

    # Sobrescritura del método
    def a_linea(self):
        return f"Bibliotecario,{self._nombre},{self._identificacion},{self._permiso_registrar}"


# Clase Libro
class Libro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._estado = "disponible"

    def obtener_titulo(self):
        return self._titulo

    def esta_disponible(self):
        return self._estado == "disponible"

    def prestar(self):
        self._estado = "prestado"

    def mostrar_info(self):
        print(f"Libro: {self._titulo}, Autor: {self._autor}, Estado: {self._estado}")

    # Texto que se guarda en el archivo libros.txt
    def a_linea(self):
        return f"{self._titulo},{self._autor},{self._estado}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self._libros = []
        self._personas = []

    # Buscar una persona por su identificación
    def buscar_persona(self, identificacion):
        for persona in self._personas:
            if persona.obtener_identificacion() == identificacion:
                return persona
        return None

    # Buscar un libro por su título
    def buscar_libro(self, titulo):
        for libro in self._libros:
            if libro.obtener_titulo() == titulo:
                return libro
        return None

    def registrar_persona(self, persona):
        if self.buscar_persona(persona.obtener_identificacion()) is None:
            self._personas.append(persona)
        else:
            print(f"{persona.obtener_nombre()} ya está registrado")

    # Solo un bibliotecario con permiso puede registrar libros
    def registrar_libro(self, bibliotecario, libro):
        if not bibliotecario.puede_registrar():
            print(f"Error: {bibliotecario.obtener_nombre()} no tiene permiso para registrar libros")
        elif self.buscar_libro(libro.obtener_titulo()) is not None:
            print(f"El libro {libro.obtener_titulo()} ya está registrado")
        else:
            self._libros.append(libro)
            print(f"Libro registrado: {libro.obtener_titulo()}")

    def prestar_libro(self, usuario, libro):
        if libro.esta_disponible():
            libro.prestar()
            usuario.agregar_prestamo(libro.obtener_titulo())
            print(f"{usuario.obtener_nombre()} tomó prestado: {libro.obtener_titulo()}")
        else:
            print(f"El libro {libro.obtener_titulo()} ya está prestado")

    # Manejo de archivos: guardar los datos en archivos de texto
    ## Modo "w" para escribir desde cero | cada objeto devuelve su propia línea con a_linea()
    def guardar_datos(self):
        with open("personas.txt", "w", encoding="utf-8") as archivo:
            for persona in self._personas:
                archivo.write(persona.a_linea() + "\n")

        with open("libros.txt", "w", encoding="utf-8") as archivo:
            for libro in self._libros:
                archivo.write(libro.a_linea() + "\n")

        print("Datos guardados en personas.txt y libros.txt")

    # Manejo de archivos: recuperar los datos guardados
    ## Modo "r" para leer | strip() quita el salto de línea y split(",") separa los datos
    def cargar_datos(self):
        try:
            with open("personas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")

                    if datos[0] == "Usuario":
                        usuario = Usuario(datos[1], datos[2])
                        if datos[3] != "":
                            for titulo in datos[3].split(";"):
                                usuario.agregar_prestamo(titulo)
                        self._personas.append(usuario)
                    else:
                        permiso = datos[3] == "True"
                        self._personas.append(Bibliotecario(datos[1], datos[2], permiso))

            with open("libros.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")

                    libro = Libro(datos[0], datos[1])
                    if datos[2] == "prestado":
                        libro.prestar()
                    self._libros.append(libro)

            print("Datos cargados desde los archivos")

        # Si los archivos no existen todavía
        except FileNotFoundError:
            print("No hay archivos guardados, se inicia con datos vacíos")

    # Polimorfismo: cada objeto responde distinto al mismo método mostrar_info()
    def mostrar_informacion(self):
        print("\nPersonas registradas:")
        for persona in self._personas:
            persona.mostrar_info()

        print("\nLibros registrados:")
        for libro in self._libros:
            libro.mostrar_info()


# Crear la biblioteca y cargar los datos guardados
biblioteca = Biblioteca()
biblioteca.cargar_datos()

# Registrar personas
biblioteca.registrar_persona(Bibliotecario("Sofía", "1-1111-1111", True))
biblioteca.registrar_persona(Bibliotecario("Pedro", "2-2222-2222", False))
biblioteca.registrar_persona(Usuario("María", "3-3333-3333"))

bibliotecario1 = biblioteca.buscar_persona("1-1111-1111")
bibliotecario2 = biblioteca.buscar_persona("2-2222-2222")
usuario1 = biblioteca.buscar_persona("3-3333-3333")

# Registrar libros (Pedro no tiene permiso)
biblioteca.registrar_libro(bibliotecario1, Libro("Python Básico", "Ana Mora"))
biblioteca.registrar_libro(bibliotecario1, Libro("Bases de Datos", "Luis Rojas"))
biblioteca.registrar_libro(bibliotecario2, Libro("Redes", "Carla Vega"))

# Prestar un libro (si ya está prestado no se permite)
libro1 = biblioteca.buscar_libro("Python Básico")
biblioteca.prestar_libro(usuario1, libro1)

# Polimorfismo
biblioteca.mostrar_informacion()

# Guardar los datos en los archivos
biblioteca.guardar_datos()