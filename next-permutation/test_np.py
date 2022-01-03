from typing import List

from itertools import permutations


class Solution:
    def nextPermutationOriginal(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])

    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i > 0:
            j = len(nums) - 1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]

        p = i
        q = len(nums) - 1
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1


def test_A():
    nums = list(range(1, 6))
    last = None
    for perm in permutations(nums):
        if last is not None:
            Solution().nextPermutation(last)
            last = tuple(last)
            assert last == perm, f'{last} != {perm}'
        last = list(perm)
    Solution().nextPermutation(last)
    assert last == nums, f'{last} != {nums}'


def test_A0():
    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    assert nums == [1, 3, 2]


def test_A1():
    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    assert nums == [1, 2, 3]


def test_A2():
    nums = [1, 3, 2]
    Solution().nextPermutation(nums)
    assert nums == [2, 1, 3]


def test_A3():
    nums = [2, 3, 1]
    Solution().nextPermutation(nums)
    assert nums == [3, 1, 2]
