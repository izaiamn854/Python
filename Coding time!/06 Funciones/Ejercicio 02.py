from random import randint

# Función que compara el intento con el número objetivo
def comprobar_intento(numero_objetivo, intento):
    if intento < numero_objetivo:
        print("El número es más alto.")
        return False
    elif intento > numero_objetivo:
        print("El número es más bajo.")
        return False
    else:
        print("¡Has acertado!")
        return True

# Generar número aleatorio del 1 al 10
numero = randint(1, 10)

# Iniciar juego
acertado = False
while not acertado:
    intento_str = input("Adivina el número (1-10): ")
    
    # Comprobar que se ha introducido un número válido
    if intento_str.isdigit():
        intento = int(intento_str)
        if 1 <= intento <= 10:
            acertado = comprobar_intento(numero, intento)
        else:
            print("Número fuera de rango, introduce un número entre 1 y 10.")
    else:
        print("Introduce un número válido.")
