# Lista de referencia
lista = [6, 14, 11, 3, 2, 1, 15, 19]

# Función para comprobar que un número está dentro de un rango
def numeroRango(numero, minimo, maximo):
    return minimo <= numero <= maximo

# Función para comprobar si un número está dentro de una lista usando for
def numeroLista(numero, lista):
    for elem in lista:
        if elem == numero:
            return True
    return False

# Solicitar número al usuario
numero = int(input("Introduce un número del 1 al 20: "))

# Comprobar rango
if numeroRango(numero, 1, 20):
    # Comprobar si está en la lista
    if numeroLista(numero, lista):
        print(f"El número {numero} está dentro de la lista.")
    else:
        print(f"El número {numero} NO está dentro de la lista.")
else:
    print("Número fuera del rango permitido (1-20).")
