class Vehicle:
    licenseCode = ""
    serialCode  = ""
    face        = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")

class Car(Vehicle):
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

Car1=Car()
Car1.turnOnAirConditioner()
PickUp1=PickUp()
PickUp1.turnOnAirConditioner()
Van1=Van()
Van1.turnOnAirConditioner()
Estatecar1=Estatecar()
Estatecar1.turnOnAirConditioner()

