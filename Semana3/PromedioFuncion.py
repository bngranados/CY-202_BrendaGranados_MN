# Objetivo: Aplicar funciones y tuplas numéricas.

def calcular_promedio(tupla):
    return sum(tupla) / len(tupla)

notas = (85, 90, 70, 95)

promedio = calcular_promedio(notas)

print("Notas:", notas)
print("Promedio:", promedio)

if promedio >= 70:
    print("Aprueba")
else:
    print("Reprueba")