
from typing import List
from functools import reduce


def log10floor(n):
    x = 1
    k = 0
    while x <= n:
        x *= 10
        k += 1
    return k - 1


def lst_to_int(lst: List[int]) -> int:
    return reduce(lambda x, y: x * 10 + y, lst)


def gen_sequential_digit_numbers_with_k_digits(k):
    return (lst_to_int(range(i, i + k)) for i in range(1, 11-k))


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        k_min = log10floor(low) + 1
        k_max = log10floor(high) + 1
        for k in range(k_min, k_max + 1):
            yield from (n for n in gen_sequential_digit_numbers_with_k_digits(k) if low <= n <= high)


class SolutionOutstanding:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return (n for k in range(log10floor(low) + 1, log10floor(high) + 1 + 1) for n in (reduce(lambda x, y: (x * 10 + y), range(i, i + k)) for i in range(1, 11-k)) if low <= n <= high)


Solution = SolutionOutstanding


def test_log10floor():
    assert log10floor(101) == 2
    assert log10floor(100) == 2
    assert log10floor(99) == 1


def test_list_to_int():
    assert lst_to_int([1, 2, 3]) == 123


def test_gen_sequential_digit_numbers_with_k_digits():
    assert list(gen_sequential_digit_numbers_with_k_digits(3)) == [123, 234, 345, 456, 567, 678, 789]


def test_A0():
    assert list(Solution().sequentialDigits(100, 300)) == [123, 234]


def test_A1():
    assert list(Solution().sequentialDigits(1000, 13000)) == [1234, 2345, 3456, 4567, 5678, 6789, 12345]


def test_A2():
    assert list(Solution().sequentialDigits(8511, 23553)) == [12345, 23456]
