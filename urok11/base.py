"""
Доработайте класс `Vehicle`
"""

from abc import ABC
from urok11 import exceptions

class Vehicle(ABC):
    weight: float = 0
    started: bool = False
    fuel: float = 0
    fuel_consumption: float = 0

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError("Не хватает топлива для старта.")

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
        else:
            raise exceptions.NotEnoughFuel("Не хватает топлива для движения.")
