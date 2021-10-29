from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def adjacent(i, j):
            for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newi, newj = i+ii, j+jj
                if 0 <= newi < m and 0 <= newj < n:
                    yield newi, newj

        fresh = set((i, j) for (i, row) in enumerate(grid)
                    for (j, elem) in enumerate(row)
                    if elem == 1)
        rotten = set((i, j) for (i, row) in enumerate(grid)
                     for (j, elem) in enumerate(row)
                     if elem == 2)

        time = 0
        while fresh:
            #print(f'fresh: {fresh} rotten: {rotten}')
            #self.draw(m, n, fresh, rotten)
            frontier = set()
            for i, j in fresh:
                if any((ii, jj) in rotten for ii, jj in adjacent(i, j)):
                    frontier.add((i, j))
            if not frontier:
                return -1
            rotten = rotten.union(frontier)
            fresh = fresh.difference(frontier)
            time += 1

        #self.draw(m, n, fresh, rotten)

        return time

    def draw(self, m, n, fresh, rotten):
        grid = [['_' for _ in range(n)] for _ in range(m)]
        for (i, j) in fresh:
            grid[i][j] = 'F'
        for (i, j) in rotten:
            grid[i][j] = 'R'
        print()
        for row in grid:
            print(''.join(row))


def test_A0():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert Solution().orangesRotting(grid) == 4


def test_A1():
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert Solution().orangesRotting(grid) == -1


def test_A2():
    grid = [[0, 2]]
    assert Solution().orangesRotting(grid) == 0
