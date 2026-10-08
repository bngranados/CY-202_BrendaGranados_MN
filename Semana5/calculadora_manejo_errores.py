# Ejercicio Guiado 2 - Calculadora con manejo de errores

try:
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))
    resultado = numero1 / numero2
    print(f"Resultado: {resultado}")
except ValueError:
    print("Error: ingrese solo numeros.")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
finally:
    print("Operacion finalizada")