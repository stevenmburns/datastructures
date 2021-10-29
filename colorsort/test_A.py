
from typing import List
from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for k in [0,1,2]:
            for j in range(i,len(nums)):
                if nums[j] == k:
                    nums[i],nums[j] = nums[j],nums[i]
                    i += 1

    def sortColorsAlt(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tbl = defaultdict(int)
        for x in nums:
            tbl[x] += 1

        i = 0
        for k in [0,1,2]:
            for _ in range(tbl[k]):
                nums[i] = k
                i += 1

from hypothesis import given, example
import hypothesis.strategies as st

@given(st.lists(st.sampled_from([0,1,2])))
def test_one(nums):
    sorted_nums = nums[:]
    print(nums)
    sorted_nums.sort()
    Solution().sortColors(nums)
    assert nums == sorted_nums

@given(st.lists(st.sampled_from([0,1,2])))
def test_alt(nums):
    sorted_nums = nums[:]
    print(nums)
    sorted_nums.sort()
    Solution().sortColorsAlt(nums)
    assert nums == sorted_nums
    
