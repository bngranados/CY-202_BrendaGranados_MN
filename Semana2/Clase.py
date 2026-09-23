frutas = ["Manzana", "Pera", "Uva"]
print(frutas[0])
print(frutas[1])
print(frutas[2])
# Cada posicion almacena un valor, el indice inicia en 0

# Modificar,agregar, eleminar elementos de la lista

# Agregar

frutas.append("Naranja") # Agrega un elemento al final de la lista
print(frutas)

frutas.remove("Pera") # Elimina un elemento de la lista
print(frutas)

frutas[0] = "Sandia" # Modifica un elemento de la lista
print(frutas)

# Recorrer la lista con un ciclo for

nombre = ["Ana", "Luis", "Carlos"]

for nombre in nombre:
    print(nombre)
    
# Funciones de listas

# append() - Agrega un elemento al final de la lista
# insert() - Agrega un elemento en una posicion especifica
# extend() - Agrega los elementos de otra lista al final de la lista
# remove() - Elimina un elemento de la lista
# pop() - Elimina un elemento de la lista en una posicion especifica
# clear() - Elimina todos los elementos de la lista
# index() - Devuelve el indice de un elemento de la lista
# count() - Devuelve el numero de veces que un elemento se encuentra en la lista
# sort() - Ordena los elementos de la lista
# reverse() - Invierte el orden de los elementos de la lista
# copy() - Devuelve una copia de la lista
# len() - Devuelve el numero de elementos de la lista
# max() - Devuelve el elemento con el valor maximo de la lista
# min() - Devuelve el elemento con el valor minimo de la lista
# sum() - Devuelve la suma de los elementos de la lista
# in - verifica si un elemento se encuentra en la lista