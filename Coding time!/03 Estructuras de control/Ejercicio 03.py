# Solicitar números al usuario
inicio = int(input("Introduce el número de inicio: "))
fin = int(input("Introduce el número de fin: "))

# Inicializar sumas y contador
suma_pares = 0
suma_impares = 0
numero = inicio

while numero <= fin:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
    numero += 1

# Mostrar resultados
print(f"Los pares suman {suma_pares} y los impares {suma_impares}")
