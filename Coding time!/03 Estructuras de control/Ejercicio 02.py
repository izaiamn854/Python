# Solicitar números al usuario
inicio = int(input("Introduce el número de inicio: "))
fin = int(input("Introduce el número de fin: "))

# Inicializar suma y contador
suma_total = 0
numero = inicio

# Sumar todos los números entre inicio y fin (incluidos)
while numero <= fin:
    suma_total += numero
    numero += 1

# Mostrar el resultado
print("El resultado es:", suma_total)