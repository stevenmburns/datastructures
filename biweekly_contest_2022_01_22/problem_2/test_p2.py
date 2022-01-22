from typing import List
from itertools import accumulate


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        if len(differences) == 0:
            return 0
        a = list(accumulate(differences, initial=0))
        lb = min(a)
        ub = max(a)
        lowest_start = lower-lb
        highest_start = upper-ub
        return max(0, (highest_start-lowest_start+1))


def test_A0():
    assert Solution().numberOfArrays([1, -3, 4], 1, 6) == 2


def test_A1():
    assert Solution().numberOfArrays([3, -4, 5, 1, -2], -4, 5) == 4


def test_A2():
    assert Solution().numberOfArrays([-40], -46, 53) == 60
