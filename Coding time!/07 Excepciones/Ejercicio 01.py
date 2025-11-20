lista = [6, 14, 11, 3, 2, 1, 15, 19]

try:
    indice = int(input("Introduce la posición que quieres consultar: "))
    print(f"El valor en la posición {indice} es: {lista[indice]}")
except IndexError:
    print("Error: la posición indicada no existe en la lista.")
except ValueError:
    print("Error: debes introducir un número entero.")