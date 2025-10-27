# Solicitar un número al usuario
numero = float(input("Introduce un número: "))

# Comprobar si es positivo, negativo o cero
if numero > 0:
    print("Es un número positivo.")
elif numero == 0:
    print("Es igual a cero.")
else:
    print("Es un número negativo.")
