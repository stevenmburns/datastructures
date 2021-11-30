from typing import List

from itertools import islice, cycle


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        str = [""] * (2 * n)

        def aux(pos, n, open, close):
            nonlocal str
            if(close == n):
                yield ''.join(str)

            else:
                if(open > close):
                    str[pos] = ')'
                    yield from aux(pos + 1, n, open, close + 1)
                if(open < n):
                    str[pos] = '('
                    yield from aux(pos + 1, n, open + 1, close)

        return list(aux(0, n, 0, 0))


class SolutionKnuth:
    def generateParenthesis(self, n: int) -> List[str]:

        def reset_parens():
            return cycle('()')

        def gen():
            lst = [')'] + list(islice(reset_parens(), 2*n))
            m = 2*n-1
            while True:
                yield lst
                assert lst[m] == '('
                assert all(lst[k] == ')' for k in range(m+1, 2*n+1)), (''.join(lst[1:]), m)

                lst[m] = ')'
                if lst[m-1] == ')':
                    lst[m-1] = '('
                    m -= 1
                else:
                    j, k = m-1, 2*n-1
                    while lst[j] == '(':
                        lst[j], lst[k] = ')', '('
                        j, k = j-1, k-2

                    if j == 0:
                        break

                    lst[j] = '('
                    m = 2*n-1

        if n == 1:
            return ['()']

        return list(''.join(x[1:]) for x in gen())

class SolutionKnuthOrigin0:
    def generateParenthesis(self, n: int) -> List[str]:

        def gen():
            lst = list(islice(cycle('()'), 2*n))
            m = 2*n-2
            while True:
                yield lst
                assert lst[m] == '('
                assert all(lst[k] == ')' for k in range(m+1, 2*n)), (''.join(lst), m)

                lst[m] = ')'
                if m > 0 and lst[m-1] == ')':
                    lst[m-1] = '('
                    m -= 1
                else:
                    j, k = m-1, 2*n-2
                    while j >= 0 and lst[j] == '(':
                        assert j == 0 or m+1 <= k < 2*n
                        lst[j], lst[k] = ')', '('
                        j, k = j-1, k-2

                    if j == -1:
                        break

                    lst[j] = '('
                    m = 2*n-2

        return list(''.join(x) for x in gen())



def test_A0():
    s = SolutionKnuthOrigin0()
    r = s.generateParenthesis(3)
    print(r)
