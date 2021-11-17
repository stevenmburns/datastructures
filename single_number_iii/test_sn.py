from typing import List

from collections import Counter
from functools import reduce

from hypothesis import given, example
from hypothesis.strategies import integers


def tobin(x: int):
    return bin(x + (1 << 8) if x < 0 else x)


class Solution:
    def singleNumberSimple(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v == 1]

    def singleNumberAlt(self, nums: List[int]) -> List[int]:
        a = reduce(lambda x, y: x ^ y, nums, 0)
        aa = a & ~(a-1)  # First bit set
        #print(f"a: {tobin(a)} {tobin(a-1)} {tobin(aa)}")
        x = reduce(lambda x, y: x ^ y, [x for x in nums if aa & x], 0)
        return [x, a ^ x]

    def singleNumber(self, nums: List[int]) -> List[int]:
        a1 = reduce(lambda x, y: x ^ y, nums, 0)
        a2 = reduce(lambda x, y: x ^ y, [x**2 for x in nums], 0)
        return [[x, y] for x in nums if x**2 ^ (y := x ^ a1)**2 == a2][0]


@given(integers(min_value=-64, max_value=64), integers(min_value=-64, max_value=64))
@example(1, 3)
def test_A0(u, v):
    #print(u, v)
    if True and u != v:
        lst = Solution().singleNumberAlt([u, v])
        assert lst == [u, v] or lst == [v, u]
