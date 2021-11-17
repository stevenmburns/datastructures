from bisect import bisect_left
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        def g():
            for i in range(0, n-2):
                for j in range(i+1, n-1):
                    ps = nums[i] + nums[j]
                    # closest is either b-1 or b
                    b = bisect_left(nums, target - ps, j+1, n)
                    yield from (ps + nums[k] for k in [b-1, b] if j+1 <= k < n)

        return min(((abs(s-target), s) for s in g()))[1]


def test_A0():
    s = Solution()
    assert s.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert s.threeSumClosest([1, 1, 1, 0], -100) == 2
    assert s.threeSumClosest([0, 2, 1, -3], 1) == 0
    assert s.threeSumClosest([0, 0, 0], 0) == 0
    assert s.threeSumClosest([0, 0, 0], 1) == 0
    assert s.threeSumClosest([0, 0, 0], -1) == 0
    assert s.threeSumClosest([0, 0, 0], -2) == 0
    assert s.threeSumClosest([0, 0, 0], -3) == 0
