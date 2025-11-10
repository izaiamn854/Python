# Diccionario de usuarios
usuarios = {
    "iperurena": {"nombre": "Iñaki", "apellido": "Perurena", "password": "123123"},
    "fmuguruza": {"nombre": "Fermín", "apellido": "Muguruza", "password": "654321"},
    "aolaizola": {"nombre": "Aimar", "apellido": "Olaizola", "password": "123456"}
}

intentos_maximos = 3
intento = 0
acceso = False

while intento < intentos_maximos:
    usuario_input = input("Introduce el nombre de usuario: ")
    password_input = input("Introduce la contraseña: ")
    
    if usuario_input in usuarios and password_input == usuarios[usuario_input]["password"]:
        print(f"¡Bienvenido {usuarios[usuario_input]['nombre']} {usuarios[usuario_input]['apellido']}!")
        acceso = True
        break
    else:
        intentos_restantes = intentos_maximos - (intento + 1)
        print(f"Datos incorrectos. Le quedan {intentos_restantes} intentos.")
    
    intento += 1

if not acceso:
    print("Has agotado todos tus intentos.")
