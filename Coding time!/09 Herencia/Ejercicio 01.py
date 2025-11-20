class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        self.kilometros = 0

    def avanzar(self, km):
        """Método que deberá ser sobreescrito en las clases hijas."""
        pass

class Coche(Vehiculo):
    def __init__(self, matricula, marca):
        super().__init__(marca)
        self.matricula = matricula
        self.gasolina = 0.0

    def repostar(self, litros):
        self.gasolina += litros

    def avanzar(self, km):
        gasolina_necesaria = km * 0.1
        if gasolina_necesaria > self.gasolina:
            print("Es necesario repostar para recorrer la cantidad indicada de kilómetros")
        else:
            self.kilometros += km
            self.gasolina -= gasolina_necesaria

class Bicicleta(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca)
        self.km_desde_hinchado = 0
        self.ruedas_hinchadas = True

    def hinchar_ruedas(self):
        self.ruedas_hinchadas = True
        self.km_desde_hinchado = 0

    def avanzar(self, km):
        if not self.ruedas_hinchadas and self.km_desde_hinchado >= 50:
            print("Es necesario hinchar para recorrer la cantidad indicada de kms.")
        else:
            distancia_posible = km
            # Comprobar si se exceden 50 km sin hinchar
            if self.km_desde_hinchado + km > 50:
                distancia_posible = 50 - self.km_desde_hinchado
                print("Es necesario hinchar para recorrer la cantidad indicada de kms.")
            self.kilometros += distancia_posible
            self.km_desde_hinchado += distancia_posible
            if self.km_desde_hinchado >= 50:
                self.ruedas_hinchadas = False

# Prueba del código

# Coche:
coche = Coche("1122PKL", "Audi")
coche.repostar(20)
coche.avanzar(120)
print(f"Total de kms coche: {coche.kilometros}. Gasolina: {coche.gasolina}")
coche.avanzar(40)
print(f"Total de kms coche: {coche.kilometros}. Gasolina: {coche.gasolina}")

# Bicicleta
bicicleta = Bicicleta("BH")
bicicleta.avanzar(30)
print(f"Total de kms bici: {bicicleta.kilometros}")
bicicleta.avanzar(25)
print(f"Total de kms bici: {bicicleta.kilometros}")
bicicleta.hinchar_ruedas()
bicicleta.avanzar(25)
print(f"Total de kms bici: {bicicleta.kilometros}")
