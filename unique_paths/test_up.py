from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        counts = [[0 for _ in range(n)] for _ in range(m)]

        counts[0][0] = 1

        for j in range(1, n):
            counts[0][j] = counts[0][j-1]

        for i in range(1, m):
            counts[i][0] = counts[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                counts[i][j] = counts[i-1][j] + counts[i][j-1]

        return counts[m-1][n-1]


def test_A0():
    assert Solution().uniquePaths(3, 7) == 28


def test_A1():
    assert Solution().uniquePaths(1, 1) == 1
