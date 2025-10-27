# Solicitar al usuario un string
texto = input("Introduce un texto: ")

# Obtener los primeros 3 caracteres
primeros_tres = texto[:3]

# Obtener los últimos 3 caracteres usando len()
ultimos_tres = texto[len(texto)-3:]

# Combinar ambos y mostrar el resultado
resultado = primeros_tres + ultimos_tres
print("Resultado:", resultado)