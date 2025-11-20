class Poligono:
    def __init__(self, color, lados):
        self.color = color
        self.lados = lados  # lista con la longitud de los lados

    def perimetro(self):
        """Devuelve el perímetro del polígono."""
        return sum(self.lados)


class Triangulo(Poligono):
    def __init__(self, color, lados):
        if len(lados) != 3:
            raise ValueError("Un triángulo debe tener 3 lados.")
        super().__init__(color, lados)

    def forma(self):
        a, b, c = self.lados
        if a == b == c:
            return "Triángulo equilátero"
        elif a == b or a == c or b == c:
            return "Triángulo isósceles"
        else:
            return "Triángulo irregular"


class Cuadrado(Poligono):
    def __init__(self, color, lados):
        if len(lados) != 4:
            raise ValueError("Un cuadrado debe tener 4 lados.")
        super().__init__(color, lados)


# Ejemplo de uso
t1 = Triangulo("rojo", [2, 5, 2])
print(f"Es un {t1.forma()} {t1.color} con {t1.perimetro()}m de perímetro.")

c1 = Cuadrado("azul", [4, 4, 4, 4])
print(f"Cuadrado {c1.color} con {c1.perimetro()}m de perímetro.")
