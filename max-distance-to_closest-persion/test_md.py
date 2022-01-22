from sys import maxunicode


from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_diff = None
        last = None
        first = None
        for i, seat in enumerate(seats):
            if seat == 1:
                if first is None:
                    first = i
                if last is not None and (max_diff is None or max_diff < i-last):
                    max_diff = i-last
                last = i

        res = max(first, len(seats)-1-last)
        if max_diff is not None:
            return max(res, max_diff//2)
        else:
            return res


def test_A0():
    assert Solution().maxDistToClosest([0, 1, 1, 1, 0, 0, 1]) == 1


def test_A1():
    assert Solution().maxDistToClosest([1, 0, 0, 1]) == 1
