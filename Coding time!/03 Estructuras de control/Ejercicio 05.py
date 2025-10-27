# Número máximo de intentos
intentos_maximos = 3
intento = 0
acceso = False

while intento < intentos_maximos:
    usuario = input("Introduce el nombre de usuario: ")
    contrasena = input("Introduce la contraseña: ")
    
    if usuario == "root" and contrasena == "toor":
        print("¡Bienvenido!")
        acceso = True
        break
    else:
        intentos_restantes = intentos_maximos - (intento + 1)
        print(f"Datos incorrectos. Le quedan {intentos_restantes} intentos.")
    
    intento += 1

if not acceso:
    print("Has agotado todos tus intentos.")
