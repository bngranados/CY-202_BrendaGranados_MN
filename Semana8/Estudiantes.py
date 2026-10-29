# Clase Estudiante
## Atributos: nombre, carrera y edad
class Estudiante:
 
    # Constructor
    def __init__(self, nombre, carrera, edad):
        self.nombre = nombre
        self.carrera = carrera
        self.edad = edad
 
    # Metodo mostrar_informacion
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Carrera:", self.carrera)
        print("Edad:", self.edad)
 
 
# Codigo principal
 
# Solicitar: nombre, carrera y edad
nombre = input("Nombre: ")
carrera = input("Carrera: ")
edad = int(input("Edad: "))
 
# Crear un objeto
estudiante1 = Estudiante(nombre, carrera, edad)
 
# Mostrar toda la informacion
estudiante1.mostrar_informacion()
 