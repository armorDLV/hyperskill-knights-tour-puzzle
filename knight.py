from cell import Cell, CellValue


class Knight:
    def __init__(self, position: Cell, cells: dict[Cell: CellValue]):
        self.position = position
        self.cells = cells
        self.knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    def moves(self) -> list:
        result = list()
        for move in self.knight_moves:
            target = self.position + Cell(*move)
            if target in self.cells and self.cells[target] == CellValue.EMPTY:
                result.append(target)

        return result
