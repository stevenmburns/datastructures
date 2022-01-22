from itertools import combinations
from collections import defaultdict


from typing import List
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1

        lines = {}
        for i, j in combinations(range(n), 2):
            (x0, y0), (x1, y1) = points[i], points[j]
            A = y0-y1
            B = x1-x0
            C = y0*B + x0*A
            assert A*x1 + B*y1 == C

            if C < 0 or C == 0 and A < 0:
                A, B, C = -A, -B, -C

            g = gcd(*(x for x in (A, B, C) if x != 0))
            assert g > 0

            A, B, C = A//g, B//g, C//g

            if (A, B, C) not in lines:
                lines[(A, B, C)] = (i, 2)
            else:
                (ii, count) = lines[(A, B, C)]
                if i == ii:
                    lines[(A, B, C)] = (ii, count+1)

        return max(count for ii, count in lines.values())


def test_A0():
    assert Solution().maxPoints([[1, 1], [2, 2], [3, 3]]) == 3


def test_A1():
    assert Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
