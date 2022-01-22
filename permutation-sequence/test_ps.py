from itertools import permutations
from collections import deque

from hypothesis import given, example
from hypothesis.strategies import integers, tuples, just


class Solution:
    def getPermutationSlow(self, n: int, k: int) -> str:
        lst = list(permutations(range(n)))
        return ''.join(str(d+1) for d in lst[k-1])

    def getPermutation(self, n: int, k: int) -> str:

        radices = list(reversed(range(1, n+1)))

        def convert_to_mixed_radix(k):
            res = deque()
            for radix in reversed(radices):
                q, r = divmod(k, radix)
                res.appendleft(r)
                k = q
            return res

        remaining = list(range(n))
        lst = []
        for i in convert_to_mixed_radix(k-1):
            lst.append(remaining[i])
            remaining.pop(i)

        return ''.join(str(d+1) for d in lst)


def test_A0():
    assert Solution().getPermutation(3, 3) == "213"


def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)


@given(integers(min_value=1, max_value=8).flatmap(lambda n: tuples(just(n), integers(min_value=0, max_value=factorial(n)-1))))
def test_A1(t):
    n, k = t
    print(n, k)
    assert 0 <= k <= factorial(n)
    assert Solution().getPermutation(n, k) == Solution().getPermutationSlow(n, k)
