from board import Board
from board_printer import BoardPrinter
from cell import Cell
from solver import Solver


class Game:
    board: Board
    playing: bool = False

    def run(self) -> None:
        self.setup()

        while True:
            print("Do you want to try the puzzle? (y/n):")
            if (ans := input()) == 'y':
                if self.check_solution():
                    self.print_board()
                    self.play()
                    break
                else:
                    print("No solution exists!")
                    break
            elif ans == 'n':
                if solution := self.check_solution():
                    print("\nHere's the solution!")
                    self.print_board(solution)
                    break
                else:
                    print("No solution exists!")
                    break
            else:
                print("Invalid input!")

    def check_solution(self) -> list | None:
        solver = Solver()
        solution = solver.solve(self.board)
        return solution

    def setup(self):
        self.try_set_board()
        self.try_move_knight(print_board=False)
        self.playing = True

    def play(self) -> None:
        while True:
            self.try_move_knight()

            if self.board.solved():
                print("What a great tour! Congratulations!")
                break

            if self.board.no_more_moves():
                print("No more possible moves!")
                print(f"Your knight visited {self.board.total_moves()} squares!")
                break

    def print_board(self, solution=None) -> None:
        BoardPrinter(self.board, solution)

    def try_set_board(self) -> None:
        while True:
            print('Enter your board dimensions:')
            try:
                self.board = Board(self.str_to_cell(input()))
                break
            except ValueError:
                print("Invalid dimensions!")

    def try_move_knight(self, print_board=True) -> None:
        while True:
            print("Enter your next move:", end='') if self.playing else print("Enter the knight's starting position:")
            try:
                self.board.move_knight(self.str_to_cell(input()))
                if print_board:
                    self.print_board()
                break
            except ValueError:
                print("Invalid move!", end=' ') if self.playing else print("Invalid position!")

    @staticmethod
    def str_to_cell(string: str) -> Cell:
        try:
            x, y = map(int, string.split())
        except ValueError:
            raise ValueError("Invalid string: can't extract 2 integer coordinates")
        else:
            return Cell(x, y)


if __name__ == '__main__':
    Game().run()
