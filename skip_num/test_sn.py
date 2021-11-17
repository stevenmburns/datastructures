
import functools


def largest_sum_troll(nums):
    """Find largest sum without adjacent elements"""
    tbl = {}

    def aux(i):
        if i not in tbl:
            if len(nums) == i:
                return 0
            if len(nums) == i+1:
                return nums[i]
            # split on whether num[i] is included
            tbl[i] = max(nums[i] + aux(i+2), aux(i+1))
        return tbl[i]

    return aux(0)


def largest_sum_dreadful(nums):
    """Find largest sum without adjacent elements"""
    tbl = {0: 0}
    if len(nums) > 0:
        tbl[1] = nums[0]

    def aux(i):
        if i not in tbl:
            # split on whether num[i-1] is included
            tbl[i] = max(nums[i-1] + aux(i-2), aux(i-1))
        return tbl[i]

    return aux(len(nums))


def largest_sum_acceptable(nums):
    """Find largest sum without adjacent elements"""
    if not nums:
        return 0

    u, v = 0, nums[0]
    for x in nums[1:]:
        u, v = v, max(u+x, v)

    return v


def largest_sum_exceeds_expectations(nums):
    """Find largest sum without adjacent elements"""

    u, v = 0, 0
    for x in nums:
        u, v = v, max(u+x, v)

    return v


def largest_sum_outstanding(nums):
    """Find largest sum without adjacent elements"""
    return functools.reduce(lambda p, x: (p[1], max(p[0]+x, p[1])), nums, (0, 0))[1]


largest_sum = largest_sum_outstanding


def test_A0():
    """Find largest sum without adjacent elements"""
    assert largest_sum([]) == 0
    assert largest_sum([1]) == 1
    assert largest_sum([1, 2]) == 2
    assert largest_sum([1, 2, 3]) == 4
    assert largest_sum([1, 2, 3, 4]) == 6
    assert largest_sum([1, 2, 3, 4, 5]) == 9
    assert largest_sum([1, 2, 3, 4, 5, 6]) == 12
