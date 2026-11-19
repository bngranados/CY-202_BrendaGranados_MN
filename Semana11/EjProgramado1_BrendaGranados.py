# Ejercicio Programado #1: Sistema de Gestión de Figuras Geométricas

# Brenda Nazaret Granados Ramírez

# Clase padre
class FiguraGeometrica:
    def __init__(self, color):
        self._color = color

    # Las clases hijas deben implementar este método
    def calcular_area(self):
        pass

    def obtener_color(self):
        return self._color


# Clase hija Circulo
class Circulo(FiguraGeometrica):
    def __init__(self, color, radio):
        super().__init__(color)
        self._radio = radio

    def calcular_area(self):
        pi = 3.14159
        return pi * self._radio ** 2
    def obtener_descripcion(self):
        return f"Círculo | Color: {self._color} | Radio: {self._radio} | Área: {self.calcular_area():.2f}"

    def mostrar_informacion(self):
        print(self.obtener_descripcion())


# Clase hija Rectangulo
class Rectangulo(FiguraGeometrica):
    def __init__(self, color, ancho, alto):
        super().__init__(color)
        self._ancho = ancho
        self._alto = alto

    # Sobrescritura del método: ancho × alto
    def calcular_area(self):
        return self._ancho * self._alto

    def obtener_descripcion(self):
        return f"Rectángulo | Color: {self._color} | Ancho: {self._ancho} | Alto: {self._alto} | Área: {self.calcular_area():.2f}"

    def mostrar_informacion(self):
        print(self.obtener_descripcion())


# Clase hija Cuadrado
class Cuadrado(FiguraGeometrica):
    def __init__(self, color, lado):
        super().__init__(color)
        self._lado = lado

    def calcular_area(self):
        return self._lado * self._lado

    def obtener_descripcion(self):
        return f"Cuadrado | Color: {self._color} | Lado: {self._lado} | Área: {self.calcular_area():.2f}"

    def mostrar_informacion(self):
        print(self.obtener_descripcion())


# Guardar la figura y su área en el archivo figuras.txt
## Modo "a" para agregar al final sin borrar lo anterior
def guardar_figura(figura):
    with open("figuras.txt", "a", encoding="utf-8") as archivo:
        archivo.write(figura.obtener_descripcion() + "\n")

    print("Figura guardada en figuras.txt")


# Leer el archivo figuras.txt y mostrar las figuras registradas
## Modo "r" para leer | strip() quita el salto de línea
def mostrar_figuras_guardadas():
    try:
        with open("figuras.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if len(lineas) == 0:
            print("No hay figuras registradas.")
        else:
            print("\n=== FIGURAS REGISTRADAS ===")
            for linea in lineas:
                print(linea.strip())

    except FileNotFoundError:
        print("No hay figuras registradas (el archivo figuras.txt no existe).")


# Solicitar un número positivo para las dimensiones
def solicitar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("Error: el valor debe ser mayor que cero.")
        except ValueError:
            print("Error: ingrese solo números.")


# Solicitar el color de la figura (no vacío y solo letras)
def solicitar_color():
    while True:
        color = input("Color de la figura: ").strip()
        if color == "":
            print("Error: el color no puede estar vacío.")
        elif not color.replace(" ", "").isalpha():
            print("Error: el color debe contener solo letras.")
        else:
            return color


# Registrar un círculo: solicita los datos, crea el objeto, calcula el área y guarda
def registrar_circulo():
    color = solicitar_color()
    radio = solicitar_numero("Radio: ")

    circulo = Circulo(color, radio)
    circulo.mostrar_informacion()
    guardar_figura(circulo)


# Registrar un rectángulo
def registrar_rectangulo():
    color = solicitar_color()
    ancho = solicitar_numero("Ancho: ")
    alto = solicitar_numero("Alto: ")

    rectangulo = Rectangulo(color, ancho, alto)
    rectangulo.mostrar_informacion()
    guardar_figura(rectangulo)


# Registrar un cuadrado
def registrar_cuadrado():
    color = solicitar_color()
    lado = solicitar_numero("Lado: ")

    cuadrado = Cuadrado(color, lado)
    cuadrado.mostrar_informacion()
    guardar_figura(cuadrado)


# Mostrar las opciones del sistema
def mostrar_menu():
    print("\n=== SISTEMA DE FIGURAS GEOMÉTRICAS ===")
    print("1. Registrar círculo")
    print("2. Registrar rectángulo")
    print("3. Registrar cuadrado")
    print("4. Mostrar figuras guardadas")
    print("5. Salir")


# Controlar la ejecución del programa mediante el menú
def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar_circulo()
        elif opcion == "2":
            registrar_rectangulo()
        elif opcion == "3":
            registrar_cuadrado()
        elif opcion == "4":
            mostrar_figuras_guardadas()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida")


main()