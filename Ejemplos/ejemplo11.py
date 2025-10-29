numeros = [1,4,2,7,6,45,23,78]
sumatorio = 0
for numero in numeros:
    if numero % 2 != 0:
        continue
    sumatorio += numero
    print("La suma de los números pares es:", sumatorio)
else:
    print("Bucle finalizado.")