class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        v = 0
        sign = 1
        if idx < len(s):
            if s[idx] == '-':
                sign = -1
                idx += 1
            elif s[idx] == '+':
                idx += 1

        while idx < len(s) and s[idx] in '0123456789':
            d = ord(s[idx]) - ord('0')

            v = 10*v + d
            idx += 1

        return max(min(v*sign, 2**31 - 1), -2**31)


def test_A0():
    s = Solution()
    assert s.myAtoi('42') == 42
    assert s.myAtoi('   -42') == -42
    assert s.myAtoi('4193 with words') == 4193
    assert s.myAtoi('words and 987') == 0
    assert s.myAtoi('-91283472332') == -2147483648
    assert s.myAtoi('-+1') == 0
