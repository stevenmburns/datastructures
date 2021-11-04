from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def toSet(board):
            s = set()
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == 'O':
                        s.add((i, j))
            return s

        def adjacent(m, n, i, j):
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newi, newj = i + ii, j + jj
                if 0 <= newi < m and 0 <= newj < n:
                    yield newi, newj

        def on_border(m, n, i, j):
            return i == 0 or i == m - 1 or j == 0 or j == n - 1

        m, n = len(board), len(board[0])

        oset = toSet(board)

        reached = {(i, j) for i, j in oset if on_border(m, n, i, j)}

        frontier = reached

        while frontier:
            newfrontier = set()
            for i, j in frontier:
                for newi, newj in adjacent(m, n, i, j):
                    if (newi, newj) in oset:
                        newfrontier.add((newi, newj))
            frontier = newfrontier.difference(reached)
            reached = reached.union(newfrontier)

        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if (i, j) not in reached:
                    board[i][j] = 'X'


def test_A0():
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

    after = [["X", "X", "X", "X"], ["X", "X", "X", "X"],
             ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

    Solution().solve(board)
    assert board == after
