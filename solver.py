import copy
from dataclasses import dataclass

from board import Board


@dataclass
class Status:
    solved = False
    sequence = list()


class Solver:

    def __init__(self):
        self.status = Status()

    def solve(self, board: Board) -> list | None:
        self.visit_node(board, self.status)
        return self.status.sequence if self.status.solved else None

    def visit_node(self, board: Board, status: Status):
        status.sequence.append(board.knight_position)

        if board.solved():
            status.solved = True
            return

        # Get list of candidate cells sorted by move rating
        moves = [k for k in sorted(board.next_moves, key=board.next_moves.get, reverse=True)]

        while moves:
            _board = copy.deepcopy(board)
            _board.move_knight(moves.pop())
            self.visit_node(_board, status)
            if status.solved:
                return
        else:
            status.sequence.pop()
