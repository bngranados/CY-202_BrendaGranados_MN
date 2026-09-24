# Objetivo: Crear una función que calcule el promedio de 3 notas.

def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

resultado = calcular_promedio(n1, n2, n3)
print("Promedio:", resultado)