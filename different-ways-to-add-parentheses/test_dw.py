from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        tokens = []

        num = None

        for c in expression:

            if c in '+-*':
                assert num is not None
                tokens.append(num)
                tokens.append(c)
                num = None
            else:
                if num is None:
                    num = ord(c) - ord('0')
                else:
                    num = num*10 + ord(c) - ord('0')
        if num is not None:
            tokens.append(num)

        tbl = {}

        for i in range(0, len(tokens), 2):
            tbl[(i, i)] = {tokens[i]}

        for k in range(2, len(tokens), 2):
            for i in range(0, len(tokens), 2):
                j = i + k
                if 0 <= j < len(tokens):
                    s = set()
                    for l in range(i, j, 2):
                        a, b = tbl[(i, l)], tbl[(l+2, j)]
                        op = tokens[l+1]
                        if op == '+':
                            s.update(u+v for u in a for v in b)
                        elif op == '-':
                            s.update(u-v for u in a for v in b)
                        elif op == '*':
                            s.update(u*v for u in a for v in b)
                    tbl[(i, j)] = s

        return tbl[(0, len(tokens)-1)]


def test_A0():
    assert sorted(Solution().diffWaysToCompute("2-1-1")) == [0, 2]


def test_A1():
    assert sorted(Solution().diffWaysToCompute("2*3-4*5")) == sorted([-34, -10, -14, -10, 10])
