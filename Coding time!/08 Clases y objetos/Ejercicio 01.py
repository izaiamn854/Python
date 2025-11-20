class Coche:
    def __init__(self, matricula, marca, kilometros_recorridos=0.0, gasolina=0.0):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = kilometros_recorridos
        self.gasolina = gasolina

    def avanzar(self, km):
        gasolina_necesaria = km * 0.1
        if gasolina_necesaria > self.gasolina:
            print("Es necesario repostar para recorrer la cantidad indicada de kilómetros")
        else:
            self.kilometros_recorridos += km
            self.gasolina -= gasolina_necesaria
            print(f"Has avanzado {km} km. Kilómetros totales: {self.kilometros_recorridos}, Gasolina restante: {self.gasolina}")

    def repostar(self, litros):
        self.gasolina += litros
        print(f"Has repostado {litros} litros. Gasolina actual: {self.gasolina}")


# Ejemplo de uso
mi_coche = Coche("1234ABC", "Toyota", gasolina=50)
mi_coche.avanzar(50)    # gasolina = 45
mi_coche.avanzar(100)   # gasolina = 35
mi_coche.avanzar(40)    # gasolina = 31
mi_coche.avanzar(180)   # gasolina insuficiente
mi_coche.repostar(20)   # gasolina = 51
mi_coche.avanzar(180)   # ahora sí puede avanzar