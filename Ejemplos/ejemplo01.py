#Ejemplo. adivina número
import random
numero_secreto = random.randint(1, 100)
adivina = None
numero_intentos = 10
print("¡Bienvenido al juego de adivinar el número!")
while adivina != numero_secreto and numero_intentos > 0:
    adivina = int(input("Adivina un número entre 1 y 100: "))
    numero_intentos -= 1
    if adivina < numero_secreto:
        print("Demasiado bajo.")
    elif adivina > numero_secreto:
        print("Demasiado alto.")
    else:
        print("¡Felicidades! ¡Has adivinado el número!")