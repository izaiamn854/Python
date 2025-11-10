# Lista de ejemplo
lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]

# Diccionario para contar apariciones
conteo = {}

# Recorrer la lista
for numero in lista:
    if numero in conteo:
        conteo[numero] += 1
    else:
        conteo[numero] = 1

# Mostrar el resultado
print(conteo)
