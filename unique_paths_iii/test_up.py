from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def toSets(board):
            start = None
            end = None
            blanks = set()
            obstacles = set()
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == -1:
                        obstacles.add((i, j))
                    elif c == 1:
                        start = (i, j)
                    elif c == 2:
                        end = (i, j)
                    elif c == 0:
                        blanks.add((i, j))
                    else:
                        assert False, f"Bad square value at {(i,j)}"
            return start, end, obstacles, blanks

        def adjacent(m, n, i, j):
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newi, newj = i + ii, j + jj
                if 0 <= newi < m and 0 <= newj < n:
                    yield newi, newj

        m, n = len(grid), len(grid[0])

        start, end, obstacles, blanks = toSets(grid)

        remaining = blanks.copy()
        remaining.add(start)
        remaining.add(end)

        count = 0

        def dfs(u, path):
            #print(f"dfs({u}, {path})")
            # nonlocal remaining
            nonlocal count
            remaining.remove(u)
            path = path + (u,)
            if u == end and not remaining:
                assert len(path) == m * n - len(obstacles)
                # print(path)
                count += 1

            for v in adjacent(m, n, *u):
                if v not in obstacles and v in remaining:
                    dfs(v, path)
            remaining.add(u)

        dfs(start, ())

        return count


def test_A0():
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]

    assert Solution().uniquePathsIII(grid) == 2
