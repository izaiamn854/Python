diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

clave = input("Introduce la clave que quieres consultar: ")

try:
    print(f"El valor de '{clave}' es: {diccionario[clave]}")
except KeyError:
    print("Error: la clave indicada no existe en el diccionario.")
