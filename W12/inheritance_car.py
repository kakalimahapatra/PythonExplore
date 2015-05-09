# Name - Kakali Mahapatra
# Python Final exam
# Student ID - 84803
#car_84803.py


def main():
    print("Start Program")
    sedan1 = Sedan("Subcompact", "1.6", "Diesel", "sport", 4)
    sedan1.addFuel()
    sedan1.start()
    sedan1.run()
    sedan1.accelerate()
    print("sedan1 speed", sedan1.getSpeed())
    print("sedan1 fuelLevel", sedan1.getFuelLevel())
    sedan1.accelerate()
    print("sedan1 speed", sedan1.getSpeed())
    print("sedan1 fuelLevel", sedan1.getFuelLevel())
    sedan1.addFuel()
    print("sedan1 fuelLevel", sedan1.getFuelLevel())
    sedan1.stop()
    print("sedan1 fuelLevel", sedan1.getFuelLevel())
    print("sedan1 speed", sedan1.getSpeed())

    print("\n")

    suv1 = SUV("V4", "car", True, "family")
    suv1.addFuel()
    suv1.start()
    suv1.run()
    suv1.accelerate()
    print("suv1 speed", suv1.getSpeed())
    print("suv1 fuelLevel", suv1.getFuelLevel())
    suv1.accelerate()
    print("suv1 speed", suv1.getSpeed())
    print("suv1 fuelLevel", suv1.getFuelLevel())
    suv1.addFuel()
    print("suv1 fuelLevel", suv1.getFuelLevel())
    suv1.stop()
    print("suv1 fuelLevel", suv1.getFuelLevel())
    print("suv1 speed", suv1.getSpeed())


class Vehicle():

    fuelLevel = 100
    speed = 0
    color = ""
    engineOn = False

    def __init__(self, make, model, fuelType):
        self.make = make
        self.model = model
        self.fuelType = fuelType

    def getEngineOn(self):
        return self.engineOn

    def setEngineOn(self, engineOn):
        self.engineOn = engineOn

    def getFuelLevel(self):
        return self.fuelLevel

    def setFuelLevel(self, fuelLevel):
        if(fuelLevel <= 100) :
            self.fuelLevel = fuelLevel

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def getMake(self):
        return self.make

    def setMake(self, make):
        self.make = make

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def getFuelType(self):
        return self.fuelType

    def setFuelType(self, fuelType):
        self.fuelType = fuelType

    def start(self, level):
        self.setFuelLevel(self.getFuelLevel() - 10)
        self.setEngineOn(True)

    def stop(self):
        self.setEngineOn(False)

    def addFuel(self, level):
        self.setFuelLevel(self.getFuelLevel() + level)

class SUV(Vehicle):

    def __init__(self, make, model, fuelType, style):
        self.make = make
        self.model = model
        self.fuelType = fuelType
        self.style = style
        Vehicle.__init__(self, make, model, fuelType)
        
    def start(self):
        super().start(10)
        print("SUV started, fuelLevel is now " + str(self.getFuelLevel()))

    def stop(self):
        super().stop()
        print("SUV stopping")

    def run(self):
        print("SUV is running")
        self.setFuelLevel(self.getFuelLevel() - 50)

    def accelerate(self):
        self.speed = self.speed + 5
        self.fuelLevel = self.fuelLevel - 10

    def addFuel(self):
        print("SUV is fueling")
        super().addFuel(60)


class Sedan(Vehicle):

    engine = ""
    doors = ""

    def __init__(self, make, model, fuelType, style, sizeType):
        self.make = make
        self.model = model
        self.fuelType = fuelType
        self.style = style
        self.sizeType = sizeType

    def start(self):
        super().start(5)
        print("Sedan started, fuelLevel is now " + str(self.getFuelLevel()))

    def stop(self):
        super().stop()
        print("Sedan stopped")

    def run(self):
        print("Sedan is running")
        self.setFuelLevel(self.getFuelLevel() - 30)
        
    def accelerate(self):
        self.speed = self.speed + 10
        self.fuelLevel = self.fuelLevel - 7
    
    def addFuel(self):
        print("Sedan is fueling")
        super().addFuel(80)

main()
