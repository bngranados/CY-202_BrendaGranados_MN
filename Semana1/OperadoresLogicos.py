# Objetivo: Usar and, or, not.

# Solicitar usuario y contraseña al usuario

usuario = input("Digite su usuario: ")
contrasena = input("Digite su contraseña: ")

# Datos correctos
usuario_correcto = "admin"
contrasena_correcta = "12345"

# Validar usuario y contraseña
usuario_valido = usuario == usuario_correcto
contrasena_valida = contrasena == contrasena_correcta

# Usar operadores lógicos para determinar el acceso
acceso = usuario_valido and contrasena_valida
acesso = usuario_valido or contrasena_valida
acesso = not usuario_valido

# Mostrar resultado
if acceso:
    print("Acceso permitido")
else:
    print("Acceso denegado")