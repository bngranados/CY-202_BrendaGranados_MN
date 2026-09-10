# Datos correctos 

usuario_correcto = "admin"
contrasena_correcta = "12345"

#Solicitar datos al usuario
usuario = input("Digite el usuario: ")
contrasena = input("Digite la contraseña: ")

# Validar usuario y contraseña

usuario_valido = usuario == usuario_correcto
contrasena_valida = contrasena == contrasena_correcta

# Permitir acceso si ambos son correctos
acceso = usuario_valido and contrasena_valida

# Mostrar resultado

if acceso:
    print ("Acceso permitido")
else:
    print ("Acceso denegado")
    
# Los booleanos son un tipo de dato que representa valores lógicos: True (verdadero) y False (falso).