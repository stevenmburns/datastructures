from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        counts = [[0 for _ in range(n)] for _ in range(m)]

        counts[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for j in range(1, n):
            counts[0][j] = counts[0][j-1] if obstacleGrid[0][j] == 0 else 0

        for i in range(1, m):
            counts[i][0] = counts[i-1][0] if obstacleGrid[i][0] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                counts[i][j] = counts[i-1][j] + \
                    counts[i][j-1] if obstacleGrid[i][j] == 0 else 0

        return counts[m-1][n-1]


def test_A0():
    assert Solution().uniquePathsWithObstacles(
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2


def test_A1():
    assert Solution().uniquePathsWithObstacles([[1]]) == 0
