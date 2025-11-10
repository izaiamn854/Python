# Diccionario de ejemplo
diccionario = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}

# Lista para almacenar valores únicos
valores_unicos = []

# Recorrer el diccionario
for valor in diccionario.values():
    if valor not in valores_unicos:
        valores_unicos.append(valor)

# Mostrar resultado
print(valores_unicos)
