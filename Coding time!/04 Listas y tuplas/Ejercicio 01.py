# Lista inicial
lista = [12, 23, 5, 29, 92, 64]

# 1. Elimina el último número y añádelo al principio
ultimo = lista.pop()  # elimina el último
lista.insert(0, ultimo)  # lo añade al inicio
print("1", lista)

# 2. Mueve el segundo elemento a la última posición
segundo = lista.pop(1)  # elimina el segundo elemento
lista.append(segundo)  # lo añade al final
print("2", lista)

# 3. Añade el número 14 al comienzo de la lista
lista.insert(0, 14)
print("3", lista)

# 4. Suma todos los números de la lista y añade el resultado al final
suma = 0
for numero in lista:
    suma += numero
lista.append(suma)
print("4", lista)

# 5. Fusiona la lista actual con [4, 11, 32]
for numero in [4, 11, 32]:
    lista.append(numero)
print("5", lista)

# 6. Elimina todos los números impares de la lista
i = 0
while i < len(lista):
    if lista[i] % 2 != 0:
        lista.pop(i)
    else:
        i += 1
print("6", lista)

# 7. Ordena los números de la lista de forma ascendente
lista.sort()
print("7", lista)

# 8. Vacía la lista
lista.clear()
print("8", lista)
