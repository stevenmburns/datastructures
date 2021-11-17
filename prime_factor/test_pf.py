def prime_factor(n):
    '''
    Returns a list of the prime factors of n
    '''
    factors = []
    i = 2
    while i * i <= n:
        q, r = divmod(n, i)
        if r != 0:
            i += 1
        else:
            n = q
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def test_A():
    assert prime_factor(1) == []
    assert prime_factor(2) == [2]
    assert prime_factor(600851475143) == [71, 839, 1471, 6857]
