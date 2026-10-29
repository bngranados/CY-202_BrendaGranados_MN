# Clase Empleado
## Atributos: nombre, salario por hora y horas trabajadas en el mes
class Empleado:
 
    # Constructor
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas
 
    # Metodo calcular_salario_mensual
    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas
 
    # Metodo calcular_bono
    def calcular_bono(self):
        return self.calcular_salario_mensual() * 0.10
 
    # Metodo calcular_salario_total
    def calcular_salario_total(self):
        return self.calcular_salario_mensual() + self.calcular_bono()
 
    # Metodo mostrar
    def mostrar(self):
        print("Empleado:", self.nombre)
        print(f"Salario mensual: {self.calcular_salario_mensual():.2f}")
        print(f"Bono (10%): {self.calcular_bono():.2f}")
        print(f"Salario total: {self.calcular_salario_total():.2f}")
 
 
# Codigo principal
## Se crea el objeto usando el constructor y se llama a su metodo mostrar()
empleado1 = Empleado("Carlos", 3500, 160)
empleado1.mostrar()
 