from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        histo = Counter(words)

        matching = {}

        self_palindrome = []

        for k, v in histo.items():
            if k == k[::-1]:
                self_palindrome.append(k)
            else:
                if k[::-1] in histo:
                    matching[k] = k[::-1]

        count_for_matching = 0
        for k, v in matching.items():
            if k < v:
                count_for_matching += min(histo[k], histo[v])

        count_for_self_palindrome = 0
        for k in self_palindrome:
            count_for_self_palindrome += histo[k] // 2

        extra = 0
        if any(histo[k] % 2 == 1 for k in self_palindrome):
            extra = 1

        return 4*count_for_matching + 4*count_for_self_palindrome + 2*extra


def test_A0():
    assert Solution().longestPalindrome(["lc", "cl", "gg"]) == 6


def test_A1():
    assert Solution().longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]) == 8


def test_A2():
    assert Solution().longestPalindrome(["cc", "ll", "xx"]) == 2


def test_A3():
    assert Solution().longestPalindrome(["dd", "aa", "bb", "dd", "aa", "dd",
                                         "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"]) == 22
