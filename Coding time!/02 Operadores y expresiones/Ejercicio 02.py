# Solicitar números al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Realizar operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Evitar división por cero
if num2 != 0:
    division = num1 / num2
else:
    division = "Error: división por cero"

# Mostrar resultados
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)