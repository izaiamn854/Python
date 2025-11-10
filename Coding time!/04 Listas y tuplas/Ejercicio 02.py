# Crear la primera lista
lista1 = []
for i in range(5):
    numero = int(input(f"Introduce el número {i+1} de la primera lista: "))
    lista1.append(numero)

# Crear la segunda lista
lista2 = []
for i in range(5):
    numero = int(input(f"Introduce el número {i+1} de la segunda lista: "))
    lista2.append(numero)

# Crear lista con elementos en común
comunes = []
for num in lista1:
    if num in lista2 and num not in comunes:
        comunes.append(num)

# Mostrar resultado
print("Los números en común son:", comunes)
