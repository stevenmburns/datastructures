from typing import List
import functools


def cmp(s0, s1):
    if len(s0) < len(s1):
        return -1
    elif len(s1) < len(s0):
        return 1
    else:
        if s0 < s1:
            return -1
        elif s0 > s1:
            return 1
        else:
            return 0


class Rich:
    def __init__(self, s):
        self.s = s

    def __eq__(self, other):
        return self.s == self

    def __lt__(self, other):
        if len(self.s) < len(other.s):
            return True
        elif len(self.s) > len(other.s):
            return False
        else:
            return self.s < other.s


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=functools.cmp_to_key(cmp))
        return nums[-k]

    def kthLargestNumberAlt(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda s: (len(s), s))
        return nums[-k]

    def kthLargestNumberRich(self, nums: List[str], k: int) -> str:
        nums.sort(key=Rich)
        return nums[-k]


def test_kth():
    nums = ["10", "0", "100"]

    assert Solution().kthLargestNumber(nums, 3) == "0"
    assert Solution().kthLargestNumber(nums, 2) == "10"
    assert Solution().kthLargestNumber(nums, 1) == "100"


def test_alt():
    nums = ["10", "0", "100"]

    assert Solution().kthLargestNumberAlt(nums, 3) == "0"
    assert Solution().kthLargestNumberAlt(nums, 2) == "10"
    assert Solution().kthLargestNumberAlt(nums, 1) == "100"


def test_rich():
    nums = ["10", "0", "100"]

    assert Solution().kthLargestNumberRich(nums, 3) == "0"
    assert Solution().kthLargestNumberRich(nums, 2) == "10"
    assert Solution().kthLargestNumberRich(nums, 1) == "100"
