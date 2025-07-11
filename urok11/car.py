"""
Создайте класс `Car`, наследник `Vehicle`
"""
from urok11.base import Vehicle

class Car(Vehicle):
    engine = None

    def set_engine(self, engine):
        self.engine = engine
