def in_coins(money, coin_values):
    tbl = {}
    tbl[0] = tuple(0 for _ in coin_values)

    def incr_coin(q, idx):
        return q[:idx] + (q[idx]+1,) + q[idx+1:]

    for amount in range(1, money+1):
        possibilities = [incr_coin(tbl[cand], idx) for idx, coin_value in enumerate(
            coin_values) if (cand := amount - coin_value) in tbl]
        if possibilities:
            tbl[amount] = min(possibilities, key=sum)

    print(tbl)
    return tbl.get(money)


def test_A():
    assert in_coins(75, (25, 10, 5, 1)) == (3, 0, 0, 0)
    assert in_coins(79, (25, 10, 5, 1)) == (3, 0, 0, 4)
    assert in_coins(80, (25, 10, 5)) == (3, 0, 1)
    assert in_coins(151, (20, 9)) is None
    assert in_coins(152, (20, 9)) == (4, 8)
    assert in_coins(153, (20, 9)) == (0, 17)
    assert in_coins(154, (20, 9)) == (5, 6)
    assert in_coins(155, (20, 9)) == (1, 15)


def test_B():
    assert in_coins(101, (25, 10, 5, 1)) == (4, 0, 0, 1)
