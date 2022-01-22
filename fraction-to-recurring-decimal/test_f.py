thon


def test_A0():
    assert Solution().fractionToDecimal(1, 2) == "0.5"


def test_A1():
    assert Solution().fractionToDecimal(2, 1) == "2"


def test_A2():
    assert Solution().fractionToDecimal(2, 3) == "0.(6)"


def test_A3():
    assert Solution().fractionToDecimal(4, 333) == "0.(012)"


def test_A4():
    assert Solution().fractionToDecimal(1, 6) == "0.1(6)"
