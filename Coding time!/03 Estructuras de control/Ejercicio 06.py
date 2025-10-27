# Inicializar contador y variable para el mayor
contador = 0
mayor = None

while contador < 5:
    numero = float(input(f"Introduce el número {contador + 1}: "))
    
    # Comprobar si es el primero o si es mayor que el actual
    if mayor is None or numero > mayor:
        mayor = numero
    
    contador += 1

# Mostrar el número más alto
print("El número más alto es:", mayor)
