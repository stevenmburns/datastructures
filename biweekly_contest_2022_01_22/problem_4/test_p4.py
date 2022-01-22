

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = [i for i, x in enumerate(corridor) if x == 'S']
        if len(seats) % 2 != 0:
            return 0
        if not seats:
            return 0

        diffs = ((i-j) for i, j in zip(seats[1:], seats[:-1]))

        a = list(diffs)[1::2]
        state = 1
        for diff in diffs:
            if state == 1:
                state = 2
            elif state == 2:
                a.append(diff)
                state = 1

        assert state == 2

        prod = 1
        for x in a:
            prod *= x
            prod %= (10**9 + 7)

        return prod


def test_A0():
    assert Solution().numberOfWays("SSPPSPS") == 3


def test_A1():
    assert Solution().numberOfWays("PPSPSP") == 1


def test_A2():
    assert Solution().numberOfWays("S") == 0
