from functools import reduce


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        m = 10**9 + 7
        seats = [i for i, x in enumerate(corridor) if x == 'S']
        return 0 if not seats or len(seats) % 2 != 0 else \
            reduce(lambda x, y: x * y % m, [(i - j) for i, j in zip(seats[1:], seats[:-1])][1::2], 1)


def test_A0():
    assert Solution().numberOfWays("SSPPSPS") == 3


def test_A1():
    assert Solution().numberOfWays("PPSPSP") == 1


def test_A2():
    assert Solution().numberOfWays("S") == 0
