def sum_of_mult_3_5(n):
    """
    Returns the sum of all multiples of 3 or 5 below n.
    """
    return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])


def test_A0():
    """
    Tests sum_of_mult_3_5(n) for n = 0.
    """
    assert sum_of_mult_3_5(0) == 0
    assert sum_of_mult_3_5(10) == 23
    assert sum_of_mult_3_5(1000) == 233168
