from car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_level):
        super().__init__(make, model, year) # can sub in things like "Nissan" for "make" which would make all electric cars Nissans
        self.battery_level = battery_level
