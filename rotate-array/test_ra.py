import math
from typing import List


class SolutionExceedsExpectations:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        g = math.gcd(n, k)
        for i in range(g):
            idx1 = (i + (n//g-1)*k) % n
            tmp = nums[idx1]
            for _ in range(n//g-1):
                idx0 = idx1 - k
                if idx0 < 0:
                    idx0 += n
                nums[idx1] = nums[idx0]
                idx1 = idx0
            nums[idx1] = tmp


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return
        k %= n
        if k == 0:
            return
        g = math.gcd(n, k)
        # (n//g-1)*k = (n//g)*k - k = n*(k//g) - k = -k (mod n)
        start_idx = n-k
        for _ in range(g):
            idx1 = start_idx
            tmp = nums[idx1]
            for _ in range(n//g-1):
                idx0 = idx1 - k
                if idx0 < 0:
                    idx0 += n
                nums[idx1] = nums[idx0]
                idx1 = idx0
            nums[idx1] = tmp
            start_idx += 1
            if start_idx >= n:
                start_idx -= n


def test_A1():
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 1)
    assert nums == [7, 1, 2, 3, 4, 5, 6]


def test_A0():
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_A2():
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 2)
    assert nums == [6, 7, 1, 2, 3, 4, 5]


def test_A3():
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    Solution().rotate(nums, 2)
    assert nums == [7, 8, 1, 2, 3, 4, 5, 6]
