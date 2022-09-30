class NotEnoughFuel(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class NegativeNumber:
    def __init__(self, message):
        Exception.__init__(self, message)

class Car:
    def __init__(self, consumption = 1.0, fuel = 1000.0):
        self.consumption = consumption
        self.fuel = fuel
        self.traveled = 0
    def __str__(self):
        return f'Расход: {self.consumption} Fuel: {self.fuel}'

    def go(self, distance=1):
        counted_consumption = self.consumption * distance
        if self.fuel < counted_consumption:
            raise Exception('Не хватает топлива!')
        if distance < 0:
            raise Exception('Отрицательное растояние')
        self.fuel -= counted_consumption
        self.traveled += distance

car1 = Car(consumption=0.1, fuel = 2000)
print(car1)
car1.go(201)
print(car1)
