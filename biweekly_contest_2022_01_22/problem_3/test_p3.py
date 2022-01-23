
from typing import List


class Solution:
    def highestRankedKItems(self, grid: List[List[int]],
                            pricing: List[int],
                            start: List[int],
                            k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        reachable = set()
        i, j = start
        frontier, dist = {(i, j)}, []
        if pricing[0] <= grid[i][j] <= pricing[1]:
            dist.append(((i, j), 0))

        def adjacent(pos):
            i, j = pos
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n:
                    if grid[ii][jj] > 0:
                        yield ii, jj

        count = 0
        while frontier and len(dist) < k:
            newfrontier = {q for p in frontier for q in adjacent(p)}
            reachable.update(frontier)
            frontier = newfrontier.difference(reachable)
            count += 1
            for i, j in frontier:
                if pricing[0] <= grid[i][j] <= pricing[1]:
                    dist.append(((i, j), count))

        def sort_key(el):
            (i, j), d = el
            return d, grid[i][j], i, j

        return [list(pos) for pos, d in sorted(dist, key=sort_key)[:k]]


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
