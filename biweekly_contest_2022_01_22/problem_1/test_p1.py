
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort()
        j = n-1
        res = 0
        while j >= 0:
            res += cost[j]
            j -= 1
            if j >= 0:
                res += cost[j]
                j -= 1
            if j >= 0:
                j -= 1
        return res
        ...


def test_A0():
    assert Solution().minimumCost([1, 2, 3]) == 5


def test_A1():
    assert Solution().minimumCost([6, 5, 7, 9, 2, 2]) == 23


def test_A2():
    assert Solution().minimumCost([5, 5]) == 10
