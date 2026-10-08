# Ejercicio Guiado 1 - Analisis de notas de clase

notas = [85, 60, 92, 45, 78]

promedio = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)

aprobados = []
reprobados = []

for nota in notas:
    if nota >= 70:
        aprobados.append(nota)
    else:
        reprobados.append(nota)

print("Notas:", notas)
print(f"Promedio: {promedio:.1f}")
print("Nota maxima:", nota_maxima)
print("Nota minima:", nota_minima)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)