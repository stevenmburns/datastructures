from typing import List
from itertools import product


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def adjacent(j):
            for dj in [-1, 0, 1]:
                jj = j+dj
                if 0 <= jj < n:
                    yield jj

        dp0 = [[None for _ in range(n)] for _ in range(n)]
        dp0[0][n-1] = grid[0][0] + grid[0][n-1]

        for i in range(1, m):
            dp1 = [[None for _ in range(n)] for _ in range(n)]
            for j0, j1 in product(range(n), range(n)):
                for jj0, jj1 in product(adjacent(j0), adjacent(j1)):
                    u = dp0[j0][j1]
                    if u is not None:
                        delta = (grid[i][jj0] + grid[i][jj1]) if jj0 != jj1 else grid[i][jj0]
                        v = dp1[jj0][jj1]
                        if v is None or u+delta > v:
                            dp1[jj0][jj1] = u+delta
            dp0 = dp1

        return max(dp0[j0][j1] for j0, j1 in product(range(n), range(n)) if dp0[j0][j1] is not None)


def test_A0():
    assert 24 == Solution().cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]])


def test_A1():
    assert 28 == Solution().cherryPickup(
        [[1, 0, 0, 0, 0, 0, 1],
         [2, 0, 0, 0, 0, 3, 0],
         [2, 0, 9, 0, 0, 0, 0],
         [0, 3, 0, 5, 4, 0, 0],
         [1, 0, 2, 3, 0, 0, 6]])


def test_A2():
    assert 32 == Solution().cherryPickup(
        [[4, 1, 5, 7, 1], [6, 0, 4, 6, 4], [0, 9, 6, 3, 5]])
