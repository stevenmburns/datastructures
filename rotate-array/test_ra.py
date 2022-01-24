import math
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        g = math.gcd(n, k)
        for i in range(g):
            idx1 = (i + (n//g-1)*k) % n
            tmp = nums[idx1]
            for j in reversed(range(n//g-1)):
                idx0 = idx1 - k
                if idx0 < 0:
                    idx0 += n
                idx0a = (i + (0+j)*k) % n
                assert idx0 == idx0a
                idx1a = (i + (1+j)*k) % n
                assert idx1a == idx1
                nums[idx1] = nums[idx0]
                idx1 = idx0
            assert idx1 == i
            nums[idx1] = tmp


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
