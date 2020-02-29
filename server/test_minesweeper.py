import pytest
import numpy as np

import minesweeper

# todo make fixture to avoid repetition to av
TEST_BOARD = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]])


def test_find_neighboring_mines():
    ms = minesweeper.Game(x_max=3, y_max=3, num_mines=3)
    ms.mine_locations = TEST_BOARD
    assert ms._find_neighboring_mines(0, 0) == 0
    assert ms._find_neighboring_mines(1, 2) == 0
    assert ms._find_neighboring_mines(1, 1) == 1
    assert ms._find_neighboring_mines(0, 2) == 1
    assert ms._find_neighboring_mines(2, 1) == 1


def test_click_on_mine():
    ms = minesweeper.Game(x_max=3, y_max=3, num_mines=3)
    ms.mine_locations = TEST_BOARD
    ms.click(0, 2)
    assert ms.has_lost


def test_click_on_non_mine_without_neighbour():
    ms = minesweeper.Game(x_max=3, y_max=3, num_mines=3)
    ms.mine_locations = TEST_BOARD
    ms.click(0, 0)
    assert ms.revealed_state[0][0] == 0


def test_click_on_non_mine_with_neighbour():
    ms = minesweeper.Game(x_max=3, y_max=3, num_mines=3)
    ms.mine_locations = TEST_BOARD
    ms.click(1, 1)
    assert ms.revealed_state[1][1] == 1
