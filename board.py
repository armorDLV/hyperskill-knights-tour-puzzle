from cell import Cell, CellValue
from knight import Knight
from validators import BoardSize


class Board:
    size = BoardSize()

    def __init__(self, size: Cell) -> None:
        self.size = size

        self.cells: dict[Cell: CellValue] = dict()
        for cell in self._iter_board():
            self.cells[cell] = CellValue.EMPTY

        self.knight_position: Cell = Cell(0, 0)
        self.next_moves: dict[Cell: int] = dict()

    def move_knight(self, cell: Cell) -> None:
        valid_cells = self.cells if self.knight_position == Cell(0, 0) else self.next_moves
        if cell in valid_cells:
            if self.knight_position != Cell(0, 0):
                self.cells[self.knight_position] = CellValue.VISITED
            self.cells[cell] = CellValue.KNIGHT
            self.knight_position = cell
            self._get_next_moves()
        else:
            raise ValueError("Invalid move!")

    def solved(self) -> bool:
        return set(self.cells.values()) == {CellValue.KNIGHT, CellValue.VISITED}

    def no_more_moves(self) -> bool:
        return len(Knight(self.knight_position, self.cells).moves()) == 0

    def total_moves(self) -> int:
        return len([x for x in self.cells.values() if x in {CellValue.KNIGHT, CellValue.VISITED}])

    def _iter_board(self) -> iter:
        return iter([Cell(x, y) for x in range(1, self.size.x + 1) for y in range(1, self.size.y + 1)])

    def _get_next_moves(self) -> None:
        self.next_moves = dict()
        for move in Knight(self.knight_position, self.cells).moves():
            count = len(Knight(move, self.cells).moves())
            self.next_moves[move] = count
