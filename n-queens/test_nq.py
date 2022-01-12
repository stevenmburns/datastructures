from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def aux(queens):
            k = len(queens)
            if k == n:
                yield ["." * i + "Q" + "." * (n - i - 1) for i in queens]
            else:
                for i in range(n):
                    if i not in queens and all(abs(i - q) != abs(k - j) for j, q in enumerate(queens)):
                        yield from aux(queens + [i])
        return aux([])


def test_A0():
    sol = Solution()
    assert set(tuple(x) for x in sol.solveNQueens(4)) == {
        (".Q..", "...Q", "Q...", "..Q."), ("..Q.", "Q...", "...Q", ".Q..")}
