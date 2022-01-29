from typing import List
from operator import __add__, __sub__, __mul__
from itertools import product


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        tokens = []
        num = None
        for c in expression:
            if c in '+-*':
                assert num is not None
                tokens.append(num)
                num = None
                tokens.append(c)
            else:
                if num is None:
                    num = ord(c) - ord('0')
                else:
                    num = num*10 + ord(c) - ord('0')
        if num is not None:
            tokens.append(num)

        ops = {'+': __add__, '-': __sub__, '*': __mul__}

        n = (len(tokens)+1) // 2

        tbl = {(i, i): [tokens[2*i]] for i in range(n)}

        for k in range(1, n):
            for i in range(n-k):
                j = i + k
                tbl[(i, j)] = [ops[tokens[2*l+1]](u, v) for l in range(i, j)
                               for u, v in product(tbl[(i, l)], tbl[(l+1, j)])]

        return tbl[(0, n-1)]


def test_A0():
    assert sorted(Solution().diffWaysToCompute("2-1-1")) == [0, 2]


def test_A1():
    assert sorted(Solution().diffWaysToCompute("2*3-4*5")) == sorted([-34, -10, -14, -10, 10])


def test_A2():
    assert sorted(
        Solution().diffWaysToCompute("2*3-4*5*6+7")) == sorted(
        [-514, -514, -442, -442, -290, -254, -254, -248, -248, -227, -227, -220, -220, -197, -197, -190, -182, -142,
         -130, -130, -130, -130, -130, -121, -121, -107, -107, -77, -74, -74, -53, -53, -53, -53, -53, -46, -46, 67, 67,
         74, 130, 130])


def test_A3():
    assert sorted(
        Solution().diffWaysToCompute("2*3-4*5*6")) == sorted(
        [-234, -234, -204, -204, -114, -114, -84, -60, -60, -60, -60, -60, 60, 60])
