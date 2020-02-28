import pytest
import numpy as np

import minesweeper

TEST_BOARD = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]])


def test_find_neighbouring_mines():
    MS = minesweeper.Game(x_max=3, y_max=3)
    MS.board = TEST_BOARD
    assert ms.test_find_neighbouring_mines(0, 0) == 0
    assert ms.test_find_neighbouring_mines(1, 2) == 0
    assert ms.test_find_neighbouring_mines(1, 1) == 1
    assert ms.test_find_neighbouring_mines(0, 2) == 1
    assert ms.test_find_neighbouring_mines(2, 1) == 1
