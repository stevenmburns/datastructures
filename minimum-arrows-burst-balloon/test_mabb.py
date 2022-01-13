from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        r, count = None, 0
        for s, e in sorted(points):
            if r is None or s > r[1]:
                r = [s, e]
                count += 1
            else:
                r = max(r[0], s), min(r[1], e)
        return count


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
