 # Clase Producto
## Atributos: nombre y precio
## Metodo: mostrar()

class Producto:
 
    # Constructor
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
 
    # Metodo mostrar
    def mostrar(self):
        print("Producto:", self.nombre)
        print("Precio:", self.precio)
 
 
# Codigo principal
producto1 = Producto("Mouse", 8500)
producto1.mostrar()
 