# Ejercicio Extra (Ejercicio 5): Sistema de biblioteca con herencia

# Brenda Nazaret Granados Ramírez

# Clase padre
class Persona:
    def __init__(self, nombre, identificacion):
        self._nombre = nombre
        self._identificacion = identificacion

    def obtener_nombre(self):
        return self._nombre

    def mostrar_info(self):
        print(f"Persona: {self._nombre}, Identificación: {self._identificacion}")


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


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self._libros = []
        self._personas = []

    def registrar_persona(self, persona):
        self._personas.append(persona)

    # Solo un bibliotecario con permiso puede registrar libros
    def registrar_libro(self, bibliotecario, libro):
        if bibliotecario.puede_registrar():
            self._libros.append(libro)
            print(f"Libro registrado: {libro.obtener_titulo()}")
        else:
            print(f"Error: {bibliotecario.obtener_nombre()} no tiene permiso para registrar libros")

    def prestar_libro(self, usuario, libro):
        if libro.esta_disponible():
            libro.prestar()
            usuario.agregar_prestamo(libro.obtener_titulo())
            print(f"{usuario.obtener_nombre()} tomó prestado: {libro.obtener_titulo()}")
        else:
            print(f"El libro {libro.obtener_titulo()} ya está prestado")

    # Polimorfismo: cada objeto responde distinto al mismo método mostrar_info()
    def mostrar_informacion(self):
        print("\nPersonas registradas:")
        for persona in self._personas:
            persona.mostrar_info()

        print("\nLibros registrados:")
        for libro in self._libros:
            libro.mostrar_info()


# Crear instancias
biblioteca = Biblioteca()

bibliotecario1 = Bibliotecario("Sofía", "1-1111-1111", True)
bibliotecario2 = Bibliotecario("Pedro", "2-2222-2222", False)
usuario1 = Usuario("María", "3-3333-3333")

biblioteca.registrar_persona(bibliotecario1)
biblioteca.registrar_persona(bibliotecario2)
biblioteca.registrar_persona(usuario1)

# Registrar libros (Pedro no tiene permiso)
libro1 = Libro("Python Básico", "Ana Mora")
libro2 = Libro("Bases de Datos", "Luis Rojas")
libro3 = Libro("Redes", "Carla Vega")

biblioteca.registrar_libro(bibliotecario1, libro1)
biblioteca.registrar_libro(bibliotecario1, libro2)
biblioteca.registrar_libro(bibliotecario2, libro3)

# Prestar libros (el segundo préstamo no se permite)
biblioteca.prestar_libro(usuario1, libro1)
biblioteca.prestar_libro(usuario1, libro1)

# Polimorfismo
biblioteca.mostrar_informacion()