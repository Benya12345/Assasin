from car import Car , NotEnoughFuel , NegativeNumber

car1 = Car(consumption=0.1, fuel=20)
print(car1)
try:
    car1.go(201)
except NotEnoughFuel:
    print('НЕ ХВАТАЕТ ТОПЛИВА')
    print(car1)
except NegativeNumber:
    print('ОТРИЦАТЕЛЬНОЕ ЧИСЛО')
    print(car1)