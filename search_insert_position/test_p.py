from typing import List
from bisect import bisect_left, bisect_right

from hypothesis import given, example
from hypothesis.strategies import integers, lists


class Solution():
    def searchInsertFast(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums)
        print("---left", nums, target)
        while lb < ub:
            assert 0 <= lb < ub <= len(nums)
            assert all(x < target for x in nums[:lb])
            assert all(x >= target for x in nums[ub:])
            #assert lb > 0 and nums[lb-1] <= target
            mid = (lb + ub - 1) // 2  # or (lb + ub) // 2
            print(lb, mid, ub)
            if nums[mid] < target:
                lb = mid + 1
            else:
                ub = mid
            assert lb <= ub

        print(lb)

        assert lb == ub
        assert all(x < target for x in nums[:lb])
        assert all(x >= target for x in nums[ub:])
        return lb

    def searchInsertRight(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums)
        print("---right", nums, target)
        while lb < ub:
            assert 0 <= lb < ub <= len(nums)
            assert all(x <= target for x in nums[:lb])
            assert all(x > target for x in nums[ub:])
            #assert lb > 0 and nums[lb-1] <= target
            mid = (lb + ub - 1) // 2  # or (lb + ub) // 2
            print(lb, mid, ub)
            if nums[mid] <= target:
                lb = mid + 1
            else:
                ub = mid
            assert lb <= ub

        print(lb)

        assert lb == ub
        assert all(x <= target for x in nums[:lb])
        assert all(x > target for x in nums[ub:])
        return lb

    def searchInsertOriginOne(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums)-1
        print("---")
        while lb <= ub:
            mid = (lb + ub + 1) // 2  # or (lb + ub) // 2
            print(lb, mid, ub)
            if nums[mid] < target:
                lb = mid + 1
            else:
                ub = mid - 1
        return lb


def test_A0():
    assert Solution().searchInsert([], 5) == 0
    assert Solution().searchInsert([1], 2) == 1
    assert Solution().searchInsert([1], 0) == 0
    assert Solution().searchInsert([1, 3], 0) == 0
    assert Solution().searchInsert([1, 3], 1) == 0
    assert Solution().searchInsert([1, 3], 2) == 1
    assert Solution().searchInsert([1, 3], 3) == 1
    assert Solution().searchInsert([1, 3], 4) == 2

    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
    assert Solution().searchInsert([1, 3, 5, 6], 0) == 0
    assert Solution().searchInsert([1, 3, 5, 6], 1) == 0
    assert Solution().searchInsert([1, 3, 3, 5, 6], 3) == 1


@given(lists(integers(min_value=1, max_value=5), min_size=1, max_size=100), integers(min_value=0, max_value=6))
def test_A1(nums, target):
    nums.sort()
    assert Solution().searchInsert(nums, target) == bisect_left(nums, target)
    assert Solution().searchInsertRight(nums, target) == bisect_right(nums, target)
