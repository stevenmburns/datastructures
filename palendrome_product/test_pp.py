def palendrome_product():
    """
    Find the largest palindrome made from the product of two n-digit numbers.
    """
    palendrome_product = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1] and product > palendrome_product:
                palendrome_product = product
    return palendrome_product


def test_A0():
    assert palendrome_product() == 906609
