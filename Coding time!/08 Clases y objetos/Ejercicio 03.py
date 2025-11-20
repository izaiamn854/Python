class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ordenes_recibidas = ""

    def mueve(self, secuencia):
        """Recibe una secuencia de órdenes y actualiza la posición del robot."""
        for orden in secuencia:
            if orden == 'A':
                self.x += 1
            elif orden == 'R':
                self.x -= 1
            elif orden == 'I':
                self.y -= 1
            elif orden == 'D':
                self.y += 1
            else:
                print(f"Orden no válida ignorada: {orden}")
        self.ordenes_recibidas += secuencia

    def posicion_actual(self):
        """Devuelve la posición actual del robot."""
        return f"Posición actual: {self.x},{self.y}"

    def obtener_ordenes(self):
        """Devuelve todas las órdenes recibidas hasta ahora."""
        return f"Órdenes recibidas: {self.ordenes_recibidas}"

    def volver_inicio(self):
        """Calcula la secuencia necesaria para volver a la posición (0,0)."""
        secuencia = ""
        if self.x > 0:
            secuencia += "R" * self.x
        elif self.x < 0:
            secuencia += "A" * (-self.x)
        if self.y > 0:
            secuencia += "I" * self.y
        elif self.y < 0:
            secuencia += "D" * (-self.y)
        return f"Secuencia para posición inicial: {secuencia}"


# Ejemplo de uso
miRobot = Robot()

while True:
    orden = input("Introduce la orden: ")
    if orden == "fin":
        miRobot.ordenes_recibidas += "fin"
        break
    miRobot.mueve(orden)
    print(miRobot.posicion_actual())

print(miRobot.posicion_actual())
print(miRobot.obtener_ordenes())
print(miRobot.volver_inicio())
