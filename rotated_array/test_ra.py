from typing import List

from bisect import bisect_left

def find_transition_troll(lst: List[int]) -> int:
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return i
    return 0

def find_transition(lst: List[int]) -> int:

    lb, ub = 0, len(lst)

    if lst[0] <= lst[-1]:
        return 0

    while lb < ub:
        mid = (lb + ub) // 2
        if mid > 0 and lst[mid-1] > lst[mid]:
            return mid
        elif lst[lb] < lst[mid]:
            lb = mid
        else:
            ub = mid

    return lb

def test_transition():
    assert find_transition([4,5,6,7,0,1,2]) == 4

def test_transition0():
    assert find_transition([0,1,2,4,5,6,7]) == 0

def test_transition1():
    assert find_transition([7,0,1,2,4,5,6]) == 1

class ShiftedArray:
    def __init__(self, lst):
        self.lst = lst
        self.transition = find_transition(lst)

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, i):
        if 0 <= i < len(self):
            return self.lst[(i + self.transition) % len(self)]
        else:
            raise IndexError

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        sa = ShiftedArray(nums)


        k = bisect_left(sa, target)

        if 0 <= k < len(sa) and sa[k] == target:
            return (k + sa.transition) % len(sa)
        else:
            return -1


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1

        while True:
            if lb > ub:
                return -1
            mid=(lb+ub)//2
            if nums[mid]==target:
                return mid
            if nums[lb]<=nums[mid]:
                if nums[lb]<=target<=nums[mid]:
                    ub = mid - 1
                else:
                    lb = mid + 1
            else:
                if nums[mid]<=target<=nums[ub]:
                    lb = mid + 1
                else:
                    ub = mid - 1

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1

        while True:
            if lb > ub:
                return -1
            mid=(lb+ub)//2
            if nums[mid]==target:
                return mid

            cond0 = nums[lb]<=nums[mid]
            cond1 = nums[mid]<=target<=nums[ub]
            cond2  = nums[lb]<=target<=nums[mid]

            if cond2 or not cond0 and  not cond1:
                ub = mid - 1
            else:
                lb = mid + 1

        


def test_A0():
    assert Solution().search([4,5,6,7,0,1,2], 0) == 4

def test_A1():
    assert Solution().search([5,1,3], 5) == 0

