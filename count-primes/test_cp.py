class SolutionTroll:
    def countPrimes(self, n: int) -> int:
        a = [True] * n

        for i in range(2, n//2+1):
            if not a[i]:
                continue

            for j in range(2*i, n, i):
                a[j] = False

        return sum((1 if x else 0) for x in a[2:])


class Solution:
    def countPrimes(self, n: int) -> int:

        a = [True] * n

        for i in range(2, n//2+1):
            if i*i > n:
                continue
            if not a[i]:
                continue

            for j in range(2*i, n, i):
                a[j] = False

        return sum((1 if x else 0) for x in a[2:])


def test_A0():
    assert Solution().countPrimes(10) == 4


def test_A1():
    assert Solution().countPrimes(100) == 25


def test_A2():
    assert Solution().countPrimes(1000) == 168


def test_A3():
    assert Solution().countPrimes(499979) == 41537


def test_A4():
    assert Solution().countPrimes(5000000) == 348513
