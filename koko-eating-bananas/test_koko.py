from typing import List
from collections import Counter
import heapq


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def f(k):
            return sum((pile+k-1)//k for pile in piles)

        lo, hi = 1, sum(piles)
        while lo < hi:
            mi = (lo+hi)//2
            if f(mi) > h:
                lo = mi+1
            else:
                hi = mi

        return lo


class SolutionWithCounter:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        histo, lo, hi = Counter(piles), 1, sum(piles)
        while lo < hi:
            m = (lo+hi)//2
            if sum(count*((k+m-1)//m) for k, count in histo.items()) > h:
                lo = m+1
            else:
                hi = m
        return lo


class SolutionCheat:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        h_left = h - len(piles)
        total = sum(piles)
        hq = []

        for bananas in piles:
            hour = 1 + h_left * bananas // total
            bananas_per_hour = (bananas+hour-1) // hour
            print('push', -bananas_per_hour, bananas, hour)
            heapq.heappush(hq, (-bananas_per_hour, bananas, hour))
            h -= hour

        while h > 0:
            _, bananas, hour = heapq.heappop(hq)
            print('pop', bananas, hour)
            hour += 1
            h -= 1
            bananas_per_hour = (bananas+hour-1) // hour
            heapq.heappush(hq, (-bananas_per_hour, bananas, hour))

        return -hq[0][0]


Solution = SolutionWithCounter


def test_A0():
    assert Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4


def test_A1():
    assert Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5) == 30


def test_A2():
    assert Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6) == 23
