def factors(n):
    i = 1
    f = set()
    while i * i <= n:
        if n % i == 0:
            f.add(i)
            f.add(n//i)
        i += 1
    return f


def test_A0():
    assert factors(1) == set([1])

    i = 1
    while True:
        t = (i*(i+1))//2
        f = factors(t)
        print(t, len(f))
        if len(f) > 500:
            print(i, t)
            break
        i += 1
