from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = []
        notqueens = set(range(n))

        def aux():
            nonlocal queens, notqueens
            k = len(queens)
            if k == n:
                yield ["." * i + "Q" + "." * (n - i - 1) for i in queens]
            else:
                for i in notqueens:
                    if all(abs(i - q) != abs(k - j) for j, q in enumerate(queens)):
                        queens += [i]
                        notqueens.remove(i)
                        yield from aux()
                        queens.pop()
                        notqueens.add(i)
        return aux()


def test_A0():
    sol = Solution()
    assert set(tuple(x) for x in sol.solveNQueens(4)) == {
        (".Q..", "...Q", "Q...", "..Q."), ("..Q.", "Q...", "...Q", ".Q..")}
