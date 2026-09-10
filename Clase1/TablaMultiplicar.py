# Tabla de Multiplicar

# Objetivo: Usar bucles for

# Solicitar un numero al usuario
numero = int(input("Ingrese un numero del 1 al 10: "))


# Mostrar la tabla de multiplicar del numero ingresado
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
    