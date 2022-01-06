from typing import List
from collections import defaultdict

import sys
sys.setrecursionlimit(1000sour00)


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        d = defaultdict(list)

        for center in range(len(s)):
            for l, u in [(center, center), (center, center+1)]:
                while l >= 0 and u < len(s) and s[l] == s[u]:
                    d[l].append(u+1)
                    l -= 1
                    u += 1

        print(len(d), sum(len(v) for v in d.values()))
        print(d)

        path = []

        count = 0

        def dfs(u):
            nonlocal count
            count += 1
            if u == len(s):
                yield path[:]
            else:
                for v in d[u]:
                    path.append(s[u:v])
                    yield from dfs(v)
                    path.pop()

        res = list(dfs(0))
        print('Calls to dfs:', count)

        return res


def test_A0():
    assert Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert Solution().partition("a") == [["a"]]
    assert Solution().partition("abab") == [["a", "b", "a", "b"], ["a", "bab"], ["aba", "b"]]
    assert Solution().partition("abcd") == [["a", "b", "c", "d"]]


def test_A1():
    s = "abc" * 1000

    sol = Solution().partition(s)
    assert sol == [list(s)]


def test_A2():
    s = "aaa" + ("abc" * 10000) + "ccc"
    sol = Solution().partition(s)
    assert len(sol) == 64
