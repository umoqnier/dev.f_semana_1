class Vehicle:

    def __init__(self, color, precio, motor, combustible):
        self.color = color
        self.precio = precio
        self.motor = motor
        self.combustible = combustible

    def moverse(self):
        return "Me estoy moviendo..."

    def recargar_combustible(self):
        return "Ya recargue el combustible..."