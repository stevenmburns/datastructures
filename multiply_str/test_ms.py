

from hypothesis import given, example
from hypothesis.strategies import integers

from collections import deque


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def one_digit_multiply(num: str, digit: str) -> str:
            result = deque()
            c = 0
            for m in reversed(num):
                c, s = divmod((ord(m)-ord('0')) *
                              (ord(digit)-ord('0')) + c, 10)
                assert 0 <= s < 10
                result.appendleft(chr(s+ord('0')))
            while c > 0:
                c, s = divmod(c, 10)
                result.appendleft(chr(s+ord('0')))
            return ''.join(result)

        def add_tableau(tableau, maxlen):
            result = deque()
            c = 0
            for i in reversed(range(maxlen)):
                col_sum = sum(ord(row[i])-ord('0') for row in tableau
                              if i < len(row) and row[i] != ' ')
                c, s = divmod(col_sum + c, 10)
                result.appendleft(chr(s+ord('0')))
            while c > 0:
                c, s = divmod(c, 10)
                result.appendleft(chr(s+ord('0')))
            return ''.join(result)

        tableau = []
        for idx, m in enumerate(reversed(num2)):
            tableau.append(one_digit_multiply(num1, m) + ' ' * idx)

        maxlen = max(map(len, tableau))
        newtableau = []
        for row in tableau:
            newtableau.append(' ' * (maxlen - len(row)) + row)

        result = add_tableau(newtableau, maxlen)
        if all(c == '0' for c in result):
            return '0'
        assert result[0] != '0'
        return result


@ given(integers(min_value=0, max_value=10000), integers(min_value=0, max_value=10000))
@ example(335, 3333)
@ example(0, 3333)
def test_A0(u, v):
    print(u, v)
    assert Solution().multiply(str(u), str(v)) == str(u*v)
