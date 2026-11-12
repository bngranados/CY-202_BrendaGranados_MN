# Ejercicio 4: Animal → Perro, Gato

# Brenda Nazaret Granados Ramírez

# Clase padre
class Animal:
    def __init__(self, nombre):
        self._nombre = nombre

    def hacer_sonido(self):
        return "..."


# Clase hija Perro
class Perro(Animal):
    # Sobrescritura del método
    def hacer_sonido(self):
        return "Guau"


# Clase hija Gato
class Gato(Animal):
    # Sobrescritura del método
    def hacer_sonido(self):
        return "Miau"


# Polimorfismo (reto extra)
animales = [Perro("Rex"), Gato("Misu"), Perro("Toby")]

for animal in animales:
    print(f"{animal._nombre} dice: {animal.hacer_sonido()}")