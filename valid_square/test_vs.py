from typing import List
from itertools import combinations
from collections import Counter


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        histo = Counter((a[0]-b[0])**2+(a[1]-b[1])**2
                        for a, b in combinations((p1, p2, p3, p4), 2))

        m, M = min(histo.keys()), max(histo.keys())

        return histo[m] == 4 and histo[M] == 2 and 2*m == M


def test_A0():
    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [1, 0]
    p4 = [0, 1]
    assert Solution().validSquare(p1, p2, p3, p4) == True
