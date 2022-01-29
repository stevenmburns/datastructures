from typing import List

from collections import defaultdict, deque


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)

        ss = []

        ss = [defaultdict(list)]

        ss[0][int(num[0])] = []

        for c in num[1:]:
            y = int(c)
            s = defaultdict(list)

            for x in ss[-1]:
                s[x+y].append((x, '+'))
                s[x-y].append((x, '-'))
                s[x*y].append((x, '*'))

            print(len(s))

            ss.append(s)

        assert n == len(ss)

        for s in ss:
            print(s)

        path = deque()

        def aux(z, j):
            if j == 0:
                res = []
                for i in range(n):
                    res.append(num[i])
                    if i < n-1:
                        res.append(path[i])
                str_res = ''.join(res)
                print(str_res)
                yield str_res

            for x, op in ss[j][z]:
                path.appendleft(op)
                yield from aux(x, j-1)
                path.popleft()

        if target in ss[-1]:
            return aux(target, n-1)
        else:
            return []


def test_A0():
    assert set(Solution().addOperators('123', 6)) == {"1*2*3", "1+2+3"}


def test_A1():
    assert set(Solution().addOperators('232', 8)) == {"2*3+2", "2+3*2"}


def xtest_A2():
    assert set(Solution().addOperators('3456237490', 9191)) == set()
