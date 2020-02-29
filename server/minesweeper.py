import numpy as np
import itertools
import random


def gen_neighbor_indexes(x, y, x_max, y_max):
    neighbors = [
        (x + x_offset, y + y_offset)
        for x_offset in range(-1, 2)
        for y_offset in range(-1, 2)
    ]
    return [
        (x, y) for (x, y) in neighbors if min(x, y) >= 0 and x < x_max and y < y_max
    ]


class Game:
    """Minesweeper game state

    Attributes:
        x_max (int): number of rows of puzzle
        y_max (int): number of cols of puzzle
        num_mines (int): number of mines in puzzle
        mine_locations (array): cells in board have mine marked with 1/0
        revealed_state (array): cells in board have been revealed to have N neighbours, unrevealed = -1 marked with 1/0
        unclicked_squares (int): number of cells yet to be clicked on the board
        has_won (boon): has the player already won?
        has_lost (bool): has the plyaer already lost?

    Methods:
        click (x, y): clicks on cell and updates revealed_state, has_won & has_lost

    """

    def __init__(self, x_max=10, y_max=10, num_mines=10):
        """
        Args:
            x_max (int): number of rows of puzzle, default 10
            y_max (int): number of cols of puzzle, default 10
            num_mines (int): number of mines in puzzle, default 10
        """
        self.x_max = x_max
        self.y_max = y_max
        self.num_mines = num_mines
        self.mine_locations = np.zeros((x_max, y_max))
        self.flagged_mines = np.zeros((x_max, y_max))
        self.revealed_state = np.ones((x_max, y_max)) * -1
        self.unclicked_non_mine_count = (x_max * y_max) - num_mines
        self.unflagged_mine_count = num_mines
        self.has_won = False
        self.has_lost = False

        mine_coordinates = random.sample(
            list(itertools.product(range(x_max), range(y_max))), num_mines
        )
        for x, y in mine_coordinates:
            self.mine_locations[x][y] = 1

    def click(self, x, y):
        """
        Clicks on cell and updates revealed_state, has_won & has_lost
        
        Args:
            x: row to click
            y: col to click

        Returns:
            True if successful, False otherwise.
        """
        if self.mine_locations[x][y] == 1:
            self.has_lost = True

        else:
            self.revealed_state[x][y] = self._find_neighboring_mines(x, y)
            self.unclicked_non_mine_count -= 1
            if self.unclicked_non_mine_count == 0:
                self.has_won = True
            if self.revealed_state[x][y] == 0:
                for x_neighbour, y_neighbour in gen_neighbor_indexes(
                    x, y, self.x_max, self.y_max
                ):
                    if self.revealed_state[x_neighbour][y_neighbour] == -1:
                        self.click(x_neighbour, y_neighbour)

    def flag(self, x, y):
        """
        Clicks on cell and updates revealed_state, has_won & has_lost
        
        Args:
            x: row to click
            y: col to click

        Returns:
            True if successful, False otherwise.
        """
        self.revealed_state[x][y] = -1
        self.flagged_mines[x][y] = 1
        self.unflagged_mine_count -= 1

    def _find_neighboring_mines(self, x, y):
        """
        Finds number of neighbours of cell

        Args:
            x: cell row
            y: cell col

        Returns:
            Number of mines neigbhouring cell
        """
        total = 0
        for x_neighbour, y_neighbour in gen_neighbor_indexes(
            x, y, self.x_max, self.y_max
        ):
            total += self.mine_locations[x_neighbour][y_neighbour]
        return total - self.mine_locations[x][y]
