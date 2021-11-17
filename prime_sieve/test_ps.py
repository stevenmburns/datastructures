def prime_sieve(n):
    """
    Sieve of Eratosthenes
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False
    return primes


def test_A0():
    n = 2000000-1

    primes = [idx for idx, val in enumerate(prime_sieve(n)) if val]
    print(sum(primes))
