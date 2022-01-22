

class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        def gen_square_numbers(n):
            i = 1
            while i*i <= n:
                yield i*i
                i += 1

        aux = [False] * (n + 1)

        for j in range(1, n + 1):

            aux[j] = any((not aux[j-i] for i in gen_square_numbers(j)))

        return aux[n]


def test_A0():
    assert not Solution().winnerSquareGame(0)


def test_A1():
    assert Solution().winnerSquareGame(4)


def test_A2():
    assert Solution().winnerSquareGame(99)


def test_A3():
    assert Solution().winnerSquareGame(10000)
