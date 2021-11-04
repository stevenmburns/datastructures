from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def toSets(board):
            start = None
            end = None
            num_obstacles = 0
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == -1:
                        num_obstacles += 1
                    elif c == 1:
                        start = (i, j)
                        board[i][j] = 0
                    elif c == 2:
                        end = (i, j)
                        board[i][j] = 0
                    elif c == 0:
                        pass
                    else:
                        assert False, f"Bad square value at {(i,j)}"
            return start, end, num_obstacles

        m, n = len(grid), len(grid[0])

        start, end, num_obstacles = toSets(grid)

        count = 0

        count_remaining = m*n - num_obstacles

        def dfs(u):
            nonlocal count, count_remaining
            i, j = u
            grid[i][j] = -1
            count_remaining -= 1
            if u == end and count_remaining == 0:
                count += 1

            for newi, newj in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if 0 <= newi < m and 0 <= newj < n:
                    if grid[newi][newj] == 0:
                        dfs((newi, newj))

            grid[i][j] = 0
            count_remaining += 1

        dfs(start)

        return count


def test_A0():
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]

    assert Solution().uniquePathsIII(grid) == 2


def test_A1():
    m, n = 5, 7
    grid = [[0 for _ in range(n)] for _ in range(m)]

    grid[0][0] = 1
    grid[m-1][n-1] = 2

    assert Solution().uniquePathsIII(grid) == 1670


if __name__ == "__main__":
    test_A1()
