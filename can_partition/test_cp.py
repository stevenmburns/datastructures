from typing import List
from functools import reduce


class SolutionAcceptable:
    def canPartition(self, nums: List[int]) -> bool:
        reached = {0}

        for num in nums:
            reached.update([x + num for x in reached])

        total = sum(nums)

        return total % 2 == 0 and total // 2 in reached


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return (total := sum(nums)) % 2 == 0 and \
            ((0x1 << (total // 2)) & reduce(lambda x, y: x | (x << y), nums, 0x1)) != 0


class SolutionExceedsExpectations:
    def canPartition(self, nums: List[int]) -> bool:
        return (total := sum(nums)) % 2 == 0 and \
            total // 2 in reduce(lambda y, x: y.union([xx + x for xx in y]), nums, {0})


def test_A0():
    assert Solution().canPartition([1, 5, 11, 5]) is True
