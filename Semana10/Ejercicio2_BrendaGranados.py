# Ejercicio 2: Vehículo → Carro, Moto

# Brenda Nazaret Granados Ramírez

# Clase padre
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    def describir(self):
        print(f"Vehículo: {self._marca} {self._modelo}")


# Clase hija Carro
class Carro(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    # Sobrescritura del método
    def describir(self):
        print(f"Carro: {self._marca} {self._modelo}, Puertas: {self._puertas}")


# Clase hija Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self._cilindraje = cilindraje

    # Sobrescritura del método
    def describir(self):
        print(f"Moto: {self._marca} {self._modelo}, Cilindraje: {self._cilindraje} cc")


# Polimorfismo
vehiculo1 = Vehiculo("Genérico", "Base")
carro1 = Carro("Toyota", "Corolla", 4)
moto1 = Moto("Yamaha", "R3", 321)

vehiculos = [vehiculo1, carro1, moto1]

for vehiculo in vehiculos:
    vehiculo.describir()