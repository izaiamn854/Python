# Solicitar datos al usuario
posicion = int(input("Introduce la posición de inicio: "))
longitud = int(input("Introduce la longitud del substring: "))
frase = input("Introduce una frase: ")

# Calcular el substring
substring = frase[posicion:posicion + longitud]

# Mostrar el resultado
print("Resultado:", substring)
