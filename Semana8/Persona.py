class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print("\nInformación de la persona:")
        print(f"\nNombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        
        
        
nombre = input("\nIngrese el nombre de la persona: ")
edad = int(input("Ingrese la edad de la persona: "))

persona1 = Persona(nombre, edad)

persona1.mostrar_informacion()