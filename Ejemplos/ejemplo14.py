import random
import time

for i in range(3):
    numero_aleatorio = random.randint(1, 10)
    time.sleep(1)
    if numero_aleatorio == 5:
        print("¡Has ganado!")
        break
    else:
        print(f"Número generado: {numero_aleatorio}. Inténtalo de nuevo.")