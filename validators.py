from abc import ABC, abstractmethod

from cell import Cell


class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class BoardSize(Validator):

    def __init__(self):
        self.min_size = Cell(1, 1)
        self.max_size = Cell(30, 30)

    def validate(self, value: Cell):
        if not (self.min_size <= value <= self.max_size):
            raise ValueError("Invalid dimensions!")
