# Clase padre
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self._nombre} y tengo {self._edad} años.")


# Clase hija
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self._carrera = carrera

    # Sobrescritura del método
    def presentarse(self):
        print(
            f"Hola, mi nombre es {self._nombre}, tengo {self._edad} años "
            f"y estudio la carrera de {self._carrera}."
        )


# Polimorfismo
persona1 = Persona("Carlos", 40)
persona2 = Estudiante("Ana", 20, "Ingeniería en Sistemas")

personas = [persona1, persona2]

for persona in personas:
    persona.presentarse()