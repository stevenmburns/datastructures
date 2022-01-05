from typing import List
from collections import defaultdict


def is_palindrome(p):
    return p == p[::-1]
    l, u = 0, len(p)-1
    while l < u and p[l] == p[u]:
        l += 1
        u -= 1
    return l >= u


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        d = defaultdict(list)

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if is_palindrome(s[i:j]):
                    d[i].append(j)

        path = []

        def dfs(u):
            if u == len(s):
                yield path[:]
            else:
                for v in d[u]:
                    path.append(s[u:v])
                    yield from dfs(v)
                    path.pop()

        return list(dfs(0))


def test_palindrome():
    assert is_palindrome("")
    assert is_palindrome("a")
    assert is_palindrome("aa")
    assert is_palindrome("aba")
    assert is_palindrome("abba")
    assert not is_palindrome("ab")


def test_A0():
    assert Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"]]
