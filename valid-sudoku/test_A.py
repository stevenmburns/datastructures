from typing import List
from itertools import chain

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        assert len(board) == 9
        assert len(board[0]) == 9

        def gen_rows():
            for i in range(9):
                yield [(i,j) for j in range(9)]

        def gen_cols():
            for j in range(9):
                yield [(i,j) for i in range(9)]

        def gen_boxes():
            for i in range(0,9,3):
                for j in range(0,9,3):
                    yield [(i+ii, j+jj) for ii in range(3) for jj in range(3)]

        legal = set("123456789")

        for pairs in chain(gen_rows(), gen_cols(), gen_boxes()):
            non_empty = [board[i][j] for i, j in pairs if board[i][j] != '.']
            set_non_empty = set(non_empty)
            if len(non_empty) != len(set_non_empty) or not set_non_empty.issubset(legal):
                return False

        return True


def test_A0():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert Solution().isValidSudoku(board) == True

        