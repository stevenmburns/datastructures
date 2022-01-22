
from typing import List


class Solution:
    def highestRankedKItems(self, grid: List[List[int]],
                            pricing: List[int],
                            start: List[int],
                            k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        reachable = set()
        frontier = {tuple(start)}
        dist = {tuple(start): 0}

        def adjacent(pos):
            i, j = pos
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n:
                    if grid[ii][jj] > 0:
                        yield ii, jj

        count = 0
        while frontier:
            newfrontier = set()
            for i, j in frontier:
                for ii, jj in adjacent((i, j)):
                    newfrontier.add((ii, jj))

            reachable.update(frontier)
            frontier = newfrontier.difference(reachable)
            count += 1
            for i, j in frontier:
                assert (i, j) not in dist
                dist[(i, j)] = count

        cost_tuples = []
        for (i, j), v in dist.items():
            d = v
            p = grid[i][j]
            if pricing[0] <= p <= pricing[1]:
                cost_tuples.append((d, p, i, j))

        cost_tuples.sort()
        return [[i, j] for d, p, i, j in cost_tuples[:k]]


def test_A0():
    assert Solution().highestRankedKItems([[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]], [
        2, 5], [0, 0], 3) == [[0, 1], [1, 1], [2, 1]]


def test_A1():
    grid = [[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]]
    pricing = [2, 3]
    start = [2, 3]
    k = 2
    assert Solution().highestRankedKItems(grid, pricing, start, k) == [[2, 1], [1, 2]]


def test_A2():
    grid = [[1, 1, 1], [0, 0, 1], [2, 3, 4]]
    pricing = [2, 3]
    start = [0, 0]
    k = 3
    assert Solution().highestRankedKItems(grid, pricing, start, k) == [[2, 1], [2, 0]]
