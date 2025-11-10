# Función que determina si un número es primo
def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False
    return True

# Solicitar número al usuario
num = int(input("Introduce un número: "))

# Comprobar si es primo
if esPrimo(num):
    print(f"{num} es primo.")
else:
    print(f"{num} no es primo.")