from functools import reduce
from typing import List
from itertools import product

from collections import Counter
from bisect import bisect_right


class SolutionTroll:
    def findMaximumXOR(self, nums: List[int]) -> int:
        return max(a ^ b for a, b in product(nums, nums))


def non_empty_range(nums, lb, ub):
    lower = bisect_right(nums, lb)
    upper = bisect_right(nums, ub)

    return lower < upper or lower > 0 and nums[lower-1] == lb


def test_non_empty_range0():
    assert non_empty_range([2], 1, 10)


def test_non_empty_range1():
    assert non_empty_range([2, 3], 1, 10)


def test_non_empty_range2():
    assert non_empty_range([2, 3], 3, 10)


def test_non_empty_range3():
    assert non_empty_range([2, 3], 1, 2)


def test_non_empty_range4():
    assert not non_empty_range([2, 3], -10, 1)


def test_non_empty_range5():
    assert not non_empty_range([2, 3], 4, 10)


def test_non_empty_range6():
    assert not non_empty_range([2, 3], 1, 1)


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        histo = Counter(nums)
        nums = list(histo.keys())
        nums.sort()

        if len(nums) == 1:
            return 0

        best_xor = 0
        for j, num in reversed(list(enumerate(nums))):
            lb, ub = 0, num - 1
            for i in reversed(range(6)):
                mid = 1 << i

                print(bin(num), num, bin(mid), mid, lb, ub, nums[lb:ub])

                if num & (1 << i) != 0:
                    # we want a number that doesn't have a one here
                    if non_empty_range(nums, lb, mid-1):
                        ub = min(mid - 1, ub)
                    elif non_empty_range(nums, mid, ub):
                        lb = max(mid, lb)
                    print(f'legal_nums (no 1 in position {bin(mid)})', [bin(x) for x in nums[lb:ub]])
                else:
                    if non_empty_range(nums, mid, ub):
                        lb = max(mid, lb)
                    elif non_empty_range(nums, lb, mid-1):
                        ub = min(mid - 1, ub)
                    print(f'legal_nums (no 0 in position {bin(mid)})', [bin(x) for x in nums[lb:ub]])

        return best_xor


class SolutionCheat:

    def findMaximumXOR(self, nums):
        used_bits = reduce(lambda x, y: x | y, nums)
        i = 31
        while i >= 0 and not (used_bits & (1 << i)):
            i -= 1

        print("-----")
        print(nums, [bin(x) for x in nums])
        answer = 0
        while i >= 0:
            prefixes = {num >> i for num in nums}
            tmp = (answer << 1) | 1
            answer = (answer << 1) | any(tmp ^ p in prefixes for p in prefixes)
            print(i, answer, tmp, prefixes)
            i -= 1

        return answer


class Solution:

    def findMaximumXOR(self, nums):
        bit_mask = 1 << 31

        used_bits = reduce(lambda x, y: x | y, nums)
        while bit_mask != 0 and not (used_bits & bit_mask):
            bit_mask >>= 1

        answer = 0
        word_mask = 0
        while bit_mask != 0:
            word_mask |= bit_mask
            prefixes = {num & word_mask for num in nums}
            cand = bit_mask | answer
            # The any statement means there are two prefixes (possibly the same) that when xor together make cand
            answer = cand if any(cand ^ p in prefixes for p in prefixes) else answer
            bit_mask >>= 1

        return answer


def test_A0():
    s = Solution()
    assert s.findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28


def test_A1():
    s = Solution()
    assert s.findMaximumXOR([8, 10]) == 2


def test_A2():
    s = Solution()
    assert s.findMaximumXOR([0, 8]) == 8


def test_A4():
    s = Solution()
    assert s.findMaximumXOR([1, 2, 3, 4]) == 7
