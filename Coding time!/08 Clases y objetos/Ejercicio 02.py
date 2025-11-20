class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def mueve(self, orden):
        if orden == 'A':
            self.x += 1
        elif orden == 'R':
            self.x -= 1
        elif orden == 'I':
            self.y -= 1
        elif orden == 'D':
            self.y += 1
        elif orden != 'fin':
            print("Orden no válida. Usa A, R, I, D o 'fin' para terminar.")

    def posicion_actual(self):
        return f"Posición actual: {self.x},{self.y}"


# Ejemplo de uso
miRobot = Robot()
orden = ""
while orden != 'fin':
    orden = input("Introduce la orden: ")
    miRobot.mueve(orden)
    if orden != 'fin':
        print(miRobot.posicion_actual())