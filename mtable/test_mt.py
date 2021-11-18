from itertools import product

from hypothesis import given, example
from hypothesis.strategies import integers


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def count_less_than(a):
            s = 0
            for i in range(1, m + 1):
                s += min(a // i, n)
            return s

        lo, hi = 1, m * n
        while lo < hi:
            mid = (lo + hi) // 2
            if count_less_than(mid) < k:
                lo = mid + 1
            else:
                hi = mid

        return lo


class SolutionTroll:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lst = [x*y for (x, y) in product(range(1, m+1), range(1, n+1))]
        lst.sort()
        return lst[k-1]


@given(integers(min_value=1, max_value=10), integers(min_value=1, max_value=10), integers(min_value=1, max_value=100))
@example(3, 3, 5)
def test_A0(m, n, k):
    if k > m*n:
        k = m*n
    print(m, n, k)
    assert Solution().findKthNumber(m, n, k) == \
        SolutionTroll().findKthNumber(m, n, k)
