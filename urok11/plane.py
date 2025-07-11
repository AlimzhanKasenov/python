"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from urok11.base import Vehicle
from urok11 import exceptions

class Plane(Vehicle):
    cargo: float = 0
    max_cargo: float = 0

    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, amount):
        if self.cargo + amount > self.max_cargo:
            raise exceptions.CargoOverload("Превышение грузоподъёмности!")
        self.cargo += amount

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before
