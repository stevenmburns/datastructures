from typing import List
from heapq import heappush, heappop, heapify


class Solution:
    def trap(self, height: List[int]) -> int:

        q = [(-h, (i, i)) for i, h in enumerate(height)]
        heapify(q)

        ans = 0
        while q:
            h, (m, M) = heappop(q)
            while q and q[0][0] == h:
                _, (i0, i1) = heappop(q)
                m, M = min(m, i0), max(M, i1)

            print(h, m, M)

            if m == M and h <= 0:
                heappush(q, (h+1, (m, M)))

        return ans

        ...


def test_A0():
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_A1():
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
