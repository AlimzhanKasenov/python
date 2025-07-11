from urok11.car import Car
from urok11.engine import Engine
from urok11.plane import Plane
from urok11 import exceptions

# Тест Car+Engine
car = Car(weight=1500, fuel=50, fuel_consumption=0.1)
engine = Engine(volume=2.0, pistons=4)
car.set_engine(engine)
print(f"Car engine: {car.engine}")

# Тест start/move с ошибками
try:
    car.start()
    car.move(100)
    print(f"Осталось топлива: {car.fuel}")
except exceptions.LowFuelError:
    print("Ошибка: мало топлива для старта")
except exceptions.NotEnoughFuel:
    print("Ошибка: не хватает топлива для движения")

# Тест Plane+груз
plane = Plane(weight=4000, fuel=100, fuel_consumption=0.5, max_cargo=500)
plane.load_cargo(200)
try:
    plane.load_cargo(400)
except exceptions.CargoOverload:
    print("Ошибка: перегруз!")
print("Plane cargo после выгрузки:", plane.remove_all_cargo())
