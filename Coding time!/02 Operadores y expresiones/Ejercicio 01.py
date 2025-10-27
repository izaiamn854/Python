# Solicitar al usuario un número del 1 al 10
numero = int(input("Introduce un número del 1 al 10: "))

# Inicializar contador
i = 1

# Generar la tabla de multiplicar
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1
