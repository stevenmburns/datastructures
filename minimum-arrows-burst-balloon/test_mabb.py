from typing import List

from functools import reduce


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        return reduce(
            lambda x, y: (y[1], x[1] + 1) if x[0] is None or y[0] > x[0] else
            (y[1], x[1]) if y[1] < x[0] else (x[0], x[1]),
            sorted(points),
            (None, 0))[1]


def test_A0():
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    assert Solution().findMinArrowShots(points) == 2


def test_A1():
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert Solution().findMinArrowShots(points) == 4


def test_A2():
    points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
    # [1, 10] and [3, 9] => [3, 9]
    # [3, 9] and [4, 11] => [4, 9]
    # [4, 9] and [6, 7] => [6, 7]
    # [6, 7] and [6, 9] => [6, 7] emit
    # [8, 12] and [9, 12] => [9, 12] emit

    assert Solution().findMinArrowShots(points) == 2
