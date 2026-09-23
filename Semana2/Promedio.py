# Lista promedio de notas

# Crear una lista vacia
notas = []

# Solicitar 4 notas y guardarlas en la lista

for i in range(4):
    nota = float(input("Ingrese la nota: "))
    notas.append(nota)

# Calcular el promedio
promedio = sum(notas) / len(notas)
print("El promedio es:", promedio)

# Mostrar lista completa y promedio final
print("Notas: ", notas)
print("Promedio: ", promedio)