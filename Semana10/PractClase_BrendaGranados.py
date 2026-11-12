# Sistema de gestión de empleados

# Brenda Nazaret Granados Ramírez

# Clase padre
class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario

    def mostrar_info(self):
        print(f"Empleado: {self._nombre}, Salario: {self._salario}")


# Clase hija Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self._departamento = departamento

    # Sobrescritura del método
    def mostrar_info(self):
        print(f"Gerente: {self._nombre}, Salario: {self._salario}, Departamento: {self._departamento}")


# Clase hija Desarrollador
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self._lenguaje = lenguaje

    # Sobrescritura del método
    def mostrar_info(self):
        print(f"Desarrollador: {self._nombre}, Salario: {self._salario}, Lenguaje: {self._lenguaje}")


# Crear instancias
g = Gerente("Laura", 5000, "Recursos Humanos")
d = Desarrollador("Carlos", 4000, "Python")

g.mostrar_info()
d.mostrar_info()