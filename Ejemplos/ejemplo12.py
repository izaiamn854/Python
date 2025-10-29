numeros = [5, -10, 2, 14, 7, -3, 8, 0, 11, -6]
mayor = None

for numero in numeros:
    if mayor is None or numero > mayor:
        mayor = numero
else:
    print(f"El número más alto es: {mayor}")