import random
import time
max = 10
min = 1
contador = 0
numero_secreto = random.randint(1, 10)
time.sleep(1)

print("¡Comienza el juego! La maquina tiene 3 intento para adivinar el número secreto entre 1 y 10.")

for i in range(3):
    numero_aleatorio = random.randint(min, max)
    time.sleep(1)
    if numero_aleatorio == numero_secreto:
        print("¡Has ganado! El número secreto era:", numero_secreto)
        break
    elif numero_aleatorio > numero_secreto:
        print(f"Fallo el numero era {numero_aleatorio}. Numero de intentos {contador + 1}. El numero secreto es menor.")
        max = numero_aleatorio - 1
    elif numero_aleatorio < numero_secreto:
        print(f"Fallo el numero era {numero_aleatorio}. Numero de intentos {contador + 1}. El numero secreto es mayor.")
        min = numero_aleatorio + 1
else:
    print("¡Has perdido! El número secreto era:", numero_secreto)
