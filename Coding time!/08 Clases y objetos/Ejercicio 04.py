import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        """Devuelve el perímetro del triángulo."""
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        """Devuelve el área usando la fórmula de Herón."""
        s = self.perimetro() / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area

    def forma(self):
        """Indica si el triángulo es equilátero, isósceles o irregular."""
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Irregular"


# Ejemplo de uso
triangulo = Triangulo(5, 5, 5)
print("Perímetro:", triangulo.perimetro())
print("Área:", round(triangulo.area(), 2))
print("Forma:", triangulo.forma())

triangulo2 = Triangulo(5, 5, 8)
print("\nPerímetro:", triangulo2.perimetro())
print("Área:", round(triangulo2.area(), 2))
print("Forma:", triangulo2.forma())
