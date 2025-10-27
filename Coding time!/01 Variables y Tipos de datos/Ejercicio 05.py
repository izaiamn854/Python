# Solicitar datos al usuario
frase = input("Introduce una frase: ")
letra_original = input("Introduce la letra que quieres reemplazar: ")
letra_nueva = input("Introduce la letra por la que se reemplazará: ")

# Contar cuántas veces aparece la letra original
cantidad = frase.count(letra_original)

# Reemplazar la letra original por la nueva
frase_modificada = frase.replace(letra_original, letra_nueva)

# Mostrar resultados
print(f"{cantidad} apariciones.")
print("Frase modificada:", frase_modificada)
