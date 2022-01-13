from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[row - row % 3 + i][col - col % 3 + j] == num:
                        return False
            return True

        found = False

        def prnt():
            print("-----------------")
            for i in range(9):
                print(''.join(board[i]))

        def aux(i, j):
            nonlocal board, found

            if i == 9:
                found = True
                return

            #print('aux', i, j)
            # prnt()

            if board[i][j] == '.':
                for k in range(1, 10):
                    if is_valid(i, j, str(k)):
                        board[i][j] = str(k)
                        if j == 8:
                            aux(i + 1, 0)
                        else:
                            aux(i, j + 1)
                        if found:
                            return
                        board[i][j] = '.'
            else:
                if j == 8:
                    aux(i + 1, 0)
                else:
                    aux(i, j + 1)

        aux(0, 0)
        assert found


def test_A0():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    gold = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

    Solution().solveSudoku(board)
    assert board == gold
