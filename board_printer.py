import copy

from board import Board
from cell import Cell, CellValue


class BoardPrinter:

    def __init__(self, board: Board, solution=None):
        self._cells = copy.deepcopy(board.cells)
        self._next_moves = board.next_moves
        self._size_x = board.size.x
        self._size_y = board.size.y
        self._solution = solution

        self._cell_width = len(str(self._size_x * self._size_y))
        self._row_index_width = len(str(self._size_y))

        for cell, value in self._cells.items():
            self._cells[cell] = self._cell_str(value)

        for cell, value in self._next_moves.items():
            self._cells[cell] = self._pad(str(value))

        if self._solution:
            for i, cell in enumerate(self._solution, start=1):
                self._cells[cell] = self._pad(str(i))

        self._print()

    def _print(self):
        aux_list = list()
        aux_list.append(self._h_line())
        for y in self._iter_y():
            aux_list.append(self._row_str(y))
        aux_list.append(self._h_line())
        aux_list.append(self._cols_str())
        print('\n'.join(aux_list), end='\n\n')

    def _h_line(self) -> str:
        return ' ' * self._row_index_width + '-' * (3 + self._size_x * (self._cell_width + 1))

    def _row_str(self, y: int) -> str:
        aux_str = ' '.join([self._cells[Cell(x, y)] for x in self._iter_x()])
        index = str(y).rjust(self._row_index_width)
        return f'{index}| {aux_str} |'

    def _cols_str(self) -> str:
        aux_str = ' '.join([self._pad(str(x)) for x in self._iter_x()])
        return f'   {aux_str} '

    def _pad(self, value: str = '', filler: str = ' ') -> str:
        return value.rjust(self._cell_width, filler)

    def _iter_x(self) -> iter:
        return iter([x for x in range(1, self._size_x + 1)])

    def _iter_y(self) -> iter:
        return iter([y for y in range(1, self._size_y + 1)[::-1]])

    def _cell_str(self, value: CellValue) -> str:
        return self._pad(value.symbol(), value.filler())
