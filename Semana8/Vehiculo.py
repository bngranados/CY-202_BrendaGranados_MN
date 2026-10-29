 
# Clase Vehiculo

## Atributos: marca, modelo y anio
## Metodo: mostrar()
class Vehiculo:
 
    # Constructor
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
 
    # Metodo mostrar
    def mostrar(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Anio: {self.anio}")
 
 
# Codigo principal
 
# Crear tres objetos
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo2 = Vehiculo("Honda", "Civic", 2018)
vehiculo3 = Vehiculo("Nissan", "Sentra", 2022)
 
# Mostrar los tres objetos
vehiculo1.mostrar()
vehiculo2.mostrar()
vehiculo3.mostrar()
 