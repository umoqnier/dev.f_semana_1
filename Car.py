from Vehicle import Vehicle
from Transport import Transport


class Car(Vehicle, Transport):

    def __init__(self, color, precio, motor, combustible, placas, caballos, num_puertas):
        super().__init__(color, precio, motor, combustible)
        self.placas = placas
        self.caballos = caballos
        self.num_puertas = num_puertas


if __name__ == '__main__':
    car = Car('Rojo', "234442", "V8", "DISSEL", "465dji", "494", "4")
    print(car.moverse())
    print(car.precio)