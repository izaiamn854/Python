# Solicitar nombre de usuario y contraseña
usuario = input("Introduce el nombre de usuario: ")
contrasena = input("Introduce la contraseña: ")

# Comprobar credenciales
if usuario == "root" and contrasena == "toor":
    print("¡Bienvenido!")
else:
    print("Acceso fallido")
