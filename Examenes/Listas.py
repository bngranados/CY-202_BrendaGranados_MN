# Listas - son ordenadas, heterogeneas y mutables
# para crearlas se usan corchetes y se separan los elementos con comas  

lista = [29, True, 3.1415, "El numero de avogdro si que mola"]

# print (lista[1:3]) # con indices negativos se puede acceder a los elementos desde el final de la lista

#para modificar un elemento de la lista se hace asi
lista[3] = "Hola mundo!"
print(lista)

# Ejemplo as per semana 2

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