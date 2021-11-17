
def even_fibonacci_sum(limit):
    """
    Returns the sum of even Fibonacci numbers
    """
    a, b = 1, 2
    sum = 0
    while a < limit:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
    return sum


def test_A0():
    assert even_fibonacci_sum(4000000) == 4613732
