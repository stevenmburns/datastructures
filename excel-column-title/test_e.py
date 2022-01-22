
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = []
        while columnNumber != 0:
            columnNumber, r = divmod(columnNumber-1, 26)
            a.append(r)

        return ''.join(chr(i+ord('A')) for i in reversed(a))


def test_A0():
    assert Solution().convertToTitle(1) == 'A'


def test_A1():
    assert Solution().convertToTitle(2) == 'B'


def test_A2():
    assert Solution().convertToTitle(26) == 'Z'


def test_A3():
    assert Solution().convertToTitle(27) == 'AA'


def test_A4():
    assert Solution().convertToTitle(701) == 'ZY'
