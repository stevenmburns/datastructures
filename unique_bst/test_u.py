class Solution:
    def numTrees(self, n: int) -> int:
        tbl = {1: 1, 2: 2, 3: 5, 4: 14, 5: 42, 6: 132, 7: 429, 8: 1430, 9: 4862, 10: 16796, 11: 58786, 12: 208012,
               13: 742900, 14: 2674440, 15: 9694845, 16: 35357670, 17: 129644790, 18: 477638700, 19: 1767263190}

        def aux(n):
            if n not in tbl:
                tbl[n] = sum(aux(i) * aux(n - 1 - i) for i in range(n))
            return tbl[n]
        return aux(n)


def test_A0():
    assert Solution().numTrees(3) == 5
    r = {i: Solution().numTrees(i) for i in range(1, 20)}
    print(r)
