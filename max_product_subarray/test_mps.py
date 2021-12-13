from typing import List
from operator import mul
from functools import reduce

class SolutionTroll:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        M = 0
        for i in range(n):
            for j in range(i+1, n+1):
                M = max(M, reduce(mul, nums[i:j], 1))
                
        return M


class SolutionAcceptable:
    def maxProduct(self, nums: List[int]) -> int:
        M = nums[0]


        s = [nums[0]]

        for x in nums[1:]:
            if x == 0:
                s = [0]
            else:
                if s == [] or s == [0]:
                    s = [x]
                else:
                    s = [ x * y for y in s ]
                    if len(s) == 1:
                        if s[0] < 0 and x > 0 or \
                           s[0] > 0 and x < 0:
                            s.append(x)

            M = max(s + [M])
                
        return M

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        M = p = n = nums[0]
        for x in nums[1:]:
            p, n = max(x, x * p, x * n), min(x, x*p, x * n)
            M = max(p, M)  
        return M


def test_A0():
    assert Solution().maxProduct([2,3,-2,4]) == 6
    assert Solution().maxProduct([-2,0,-1]) == 0