# Validacion de usuarios

# Lista de usuarios permitidos
usuarios_permitidos = ["admin", "nazareth", "invitado"]

# Solicitar un usuario
usuario = input("Usuario: ")

# Verificar si el usuario esta en la lista y mostrar el resultado
if usuario in usuarios_permitidos:
    print("Acceso permitido")
else:
    print("Acceso denegado")