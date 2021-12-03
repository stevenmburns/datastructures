from typing import List
from itertools import chain

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s, max_area = [], 0
        for i, x in enumerate(chain(heights,[0])):
            print(i,x,s)
            while s and x < (h := heights[s[-1][0]]):
                
                width = i - s[-1] - 1
                area = top * width
                print('\t', top, width, area, s[-1])
                max_area = max(max_area, area)
                s.pop()
            if not s or x > top:
                s.append(i)
        return max_area

def test_A0():
    assert Solution().largestRectangleArea([2,1,5,6,2,3]) == 10

def test_A1():
    assert Solution().largestRectangleArea([2,1,2]) == 3