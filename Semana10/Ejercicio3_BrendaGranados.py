# Ejercicio 3: Empleado → Administrativo, Docente

# Brenda Nazaret Granados Ramírez

# Clase padre
class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario

    def calcular_pago(self):
        return self._salario


# Clase hija Administrativo
class Administrativo(Empleado):
    def __init__(self, nombre, salario, bono_fijo):
        super().__init__(nombre, salario)
        self._bono_fijo = bono_fijo

    # Sobrescritura del método: salario más el bono fijo
    def calcular_pago(self):
        return self._salario + self._bono_fijo


# Clase hija Docente
class Docente(Empleado):
    def __init__(self, nombre, salario, horas_catedra):
        super().__init__(nombre, salario)
        self._horas_catedra = horas_catedra

    # Sobrescritura del método: el salario es el valor por hora de cátedra
    def calcular_pago(self):
        return self._salario * self._horas_catedra


# Polimorfismo
empleado1 = Empleado("Ana", 450000)
administrativo1 = Administrativo("Carlos", 500000, 50000)
docente1 = Docente("Laura", 5000, 80)

empleados = [empleado1, administrativo1, docente1]

for empleado in empleados:
    print(f"{empleado._nombre} recibe: {empleado.calcular_pago()}")