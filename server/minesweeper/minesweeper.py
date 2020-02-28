import numpy as np
import itertools
import random


class Game:
    def __init__(self, x_max=10, y_max=10, num_mines=10):
        self.board = np.zeros((x_max, y_max))
        self.revealed_state = np.zeros((x_max, y_max))
        self.unclicked_squares = (x_max * y_max) - num_mines
        mine_locations = random.sample(
            list(itertools.product(range(x_max), range(y_max))), num_mines
        )
        for x_max, y_max in mine_locations:
            board[x_max][y_max] = 1
        self.has_won = False
        self.has_lost = True

    def click(self, x, y):
        if self.board[x][y] == 1:
            self.has_lost = True

        else:
            self.revealed_state = self.find_neighboring_mines(x, y)

    def find_neighboring_mines(self, x, y):
        total = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                x_neighbour = x + x_offset
                y_neighbour = y + y_offset
                if x_neighbour >= 0 and x_neighbour <= self.x_max:
                    if y_neighbour >= 0 and y_neighbour <= self.y_max:
                        total += self.board[x_neighbour][y_neighbour]
        return total - self.board[x][y]
