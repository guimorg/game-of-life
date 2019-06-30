import numpy as np

from scipy.ndimage import convolve


class Game:

    def sum_of_borders(
        self,
        board
    ):
        kernel = np.array([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])
        board_neighbors = convolve(board, kernel, mode='constant')
        return board_neighbors

    def next_generation(
        self,
        board
    ):
        dim_x, dim_y = board.shape
        new_board = np.zeros(shape=(dim_x, dim_y))
        board_neighbors = self.sum_of_borders(board)

        # TODO
        # Try removing nested for loops

        # Here we apply Conway's Rules to Obtain next Board!
        for x in range(dim_x):
            for y in range(dim_y):
                no_neighbors = board_neighbors[x, y]
                if board[x, y] == 1 and (no_neighbors < 2 or no_neighbors > 3):
                    new_board[x, y] = 0
                elif board[x, y] == 1:
                    new_board[x, y] = 1
                elif board[x, y] == 0 and no_neighbors == 3:
                    new_board[x, y] = 1
        return new_board

    def __repr__(self):
        return f"Conway's Game of Life Logic."
