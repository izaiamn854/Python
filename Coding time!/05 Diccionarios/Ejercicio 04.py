# Diccionario para almacenar los estudiantes
estudiantes = {}

# Introducción de datos (máximo 10 estudiantes)
contador = 1
while contador <= 10:
    nombre = input(f"Introduce el nombre del estudiante {contador} (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    try:
        nota = float(input(f"Introduce la nota de {nombre}: "))
    except ValueError:
        print("Nota inválida, introduce un número.")
        continue
    
    estudiantes[str(contador)] = {"nombre": nombre, "nota": nota}
    contador += 1

# Listas para aprobados y suspendidos
aprobados = []
suspendidos = []
suma_notas = 0

# Recorrer estudiantes para clasificar y calcular media
for est in estudiantes.values():
    suma_notas += est["nota"]
    if est["nota"] >= 5:
        aprobados.append(est["nombre"])
    else:
        suspendidos.append(est["nombre"])

# Calcular nota media
if len(estudiantes) > 0:
    nota_media = suma_notas / len(estudiantes)
else:
    nota_media = 0

# Mostrar resultados
print("Estudiantes aprobados:", aprobados)
print("Estudiantes suspendidos:", suspendidos)
print("Nota media de la clase:", round(nota_media, 2))
