class Solution:
    def intToRoman(self, num: int) -> str:
        r = [('I', 1),
             ('IV', 4), ('V', 5),
             ('IX', 9), ('X', 10),
             ('XL', 40), ('L', 50),
             ('XC', 90), ('C', 100),
             ('CD', 400), ('D', 500),
             ('CM', 900), ('M', 1000)]

        result = ''
        for c, v in reversed(r):
            while num >= v:
                result += c
                num -= v

        return result


def test_A():
    assert Solution().intToRoman(3) == "III"
    assert Solution().intToRoman(4) == "IV"
    assert Solution().intToRoman(5) == "V"
    assert Solution().intToRoman(9) == "IX"
    assert Solution().intToRoman(10091) == "MMMMMMMMMMXCI"
