
from itertools import combinations
from typing import List
from hypothesis import given, example
from hypothesis.strategies import integers, lists


class SolutionTroll:
    def maxArea(self, height: List[int]) -> int:
        return max((min(height[a], height[b])*(b-a) for a, b in combinations(range(len(height)), 2)))


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


@given(lists(integers(min_value=0, max_value=1000), min_size=2, max_size=100))
@example([1, 8, 6, 2, 5, 4, 8, 3, 7])
def test_A0(lst):
    assert Solution().maxArea(lst) == \
        SolutionTroll().maxArea(lst)
