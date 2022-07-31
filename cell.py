from enum import Enum


class Cell:
    """Represents a square in a 2D board"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        return Cell(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Cell({self.x, self.y})'

    def __str__(self):
        return f'({self.x, self.y})'

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


class CellValue(Enum):
    EMPTY = 0
    KNIGHT = 1
    VISITED = 2

    def symbol(self) -> str:
        symbols = {
            self.EMPTY: '',
            self.KNIGHT: 'X',
            self.VISITED: '*',
        }
        return symbols[self]

    def filler(self) -> str:
        fillers = {
            self.EMPTY: '_',
            self.KNIGHT: ' ',
            self.VISITED: ' ',
        }
        return fillers[self]
