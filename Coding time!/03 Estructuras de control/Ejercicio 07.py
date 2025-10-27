mayor = None  # Variable para almacenar el número más alto
exit = True

while exit:
    entrada = input("Introduce un número (o 'fin' para terminar): ")
    
    if entrada == "fin":
        exit = False
    else:
        if mayor is None or int(entrada) > mayor:
            mayor = int(entrada)

# Mostrar el número más alto
if mayor is not None:
    print("El número más alto es:", mayor)
else:
    print("No se introdujeron números.")
