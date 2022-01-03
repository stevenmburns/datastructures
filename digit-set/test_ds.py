from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        m, d = len(s), len(digits)
        res = sum(d**i for i in range(1, m))
        for idx, c in enumerate(s):
            res += sum(1 for d in digits if d < c) * d**(m-1-idx)
            if c not in digits:
                return res
        return res + 1


def test_A0():
    assert Solution().atMostNGivenDigitSet(["1", "3", "5", "7"], 100) == 20


def test_A1():
    assert Solution().atMostNGivenDigitSet(["3", "4", "8"], 4) == 2


def test_A2():
    assert Solution().atMostNGivenDigitSet(["5", "6"], 19) == 2


def test_A3():
    assert Solution().atMostNGivenDigitSet(["5", "7", "8"], 59) == 6


def test_A4():
    assert Solution().atMostNGivenDigitSet(["1", "4", "9"], 1000000000) == 29523


def test_A5():
    assert Solution().atMostNGivenDigitSet(["7"], 8) == 1
