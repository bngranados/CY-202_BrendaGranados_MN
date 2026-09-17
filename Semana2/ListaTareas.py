# Lista de tareas

# Crear una lista vacia
tareas = []

# Solicitar tareas hasta que el usuario escriba "salir"
while True:
    tarea = input("Tarea (escribe 'salir' para terminar): ")
    if tarea == "salir":
        break
    tareas.append(tarea)

# Mostrar todas las tareas registradas
print("Tareas registradas:")
for t in tareas:
    print(t)