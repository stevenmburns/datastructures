from typing import List
from itertools import combinations, product
from hypothesis import given, example
from hypothesis.strategies import integers, lists, sampled_from
from collections import deque


class SolutionTroll:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def subsets(s):
            for l in range(len(s)+1):
                yield from combinations(s, l)

        def legal_subsets(s):
            for sb in subsets(s):
                if all(a % b == 0 or b % a == 0 for a, b in combinations(sb, 2)):
                    yield sb
        r = list(sorted(max(legal_subsets(nums), key=len)))
        print('Troll', nums, r)
        return len(r)


class SolutionCheat:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        divisibleSubset = [[num] for num in nums]

        for j, i in combinations(range(len(nums)), 2):
            if (nums[i] % nums[j]) == 0 and len(divisibleSubset[i]) < len(divisibleSubset[j]) + 1:
                divisibleSubset[i] = divisibleSubset[j] + [nums[i]]

        r = max(divisibleSubset, key=len)
        print('Cheat', nums, r)

        return len(r)


class SolutionAcceptable:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        p = [(1, None) for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    p[i] = max(p[i], (p[j][0] + 1, j))

        res = deque()
        i = max(enumerate(p), key=lambda x: x[1][0])[0]

        while i is not None:
            res.appendleft(nums[i])
            i = p[i][1]

        print('Accectable', nums, res)

        return len(res)


class SolutionExceedsExpectation:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        p = [None for _ in nums]
        c = [1 for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    cand = c[j] + 1
                    if cand > c[i]:
                        p[i] = j
                        c[i] = cand

        res = deque()
        i = max(enumerate(c), key=lambda x: x[1])[0]

        while i is not None:
            res.appendleft(nums[i])
            i = p[i]

        print('Accectable', nums, res)

        return len(res)


class SolutionGraph:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums = list(set(nums))
        nums.sort()

        _bedges = [[] for _ in nums]
        _fedges = [[] for _ in nums]

        for a, b in combinations(range(len(nums)), 2):
            u, v = nums[a], nums[b]
            assert v > u
            if v % u == 0:
                _bedges[b].append(a)
                _fedges[a].append(b)

        def bedges_gen(b):
            for a in range(b):
                u, v = nums[a], nums[b]
                if v % u == 0:
                    yield a
            # yield from _bedges[b]

        def fedges_gen(a):
            for b in range(a+1, len(nums)):
                u, v = nums[a], nums[b]
                if v % u == 0:
                    yield b
            # yield from _fedges[a]

        bcounts = [sum(1 for _ in bedges_gen(b)) for b in range(len(nums))]
        delays = [None for _ in nums]

        q = deque()

        for i, bcount in enumerate(bcounts):
            if bcount == 0:
                delays[i] = 0
                q.append(i)

        while q:
            i = q.popleft()
            for j in fedges_gen(i):
                cand = delays[i] + 1
                if delays[j] is None or cand > delays[j]:
                    delays[j] = cand
                bcounts[j] -= 1
                if bcounts[j] == 0:
                    q.append(j)

        best_idx = max(enumerate(delays), key=lambda p: p[1])[0]

        result = deque()

        while True:
            result.appendleft(nums[best_idx])
            for j in bedges_gen(best_idx):
                if delays[j] + 1 == delays[best_idx]:
                    best_idx = j
                    break
            else:
                break

        print('Graph', nums, result)

        return len(result)


@given(lists(integers(min_value=1, max_value=100), min_size=1, max_size=20))
@example(list(1 << i for i in range(4)))
def test_largest_divisible_subset(nums):
    nums = list(set(nums))
    l0 = SolutionCheat().largestDivisibleSubset(nums)
    l1 = SolutionAcceptable().largestDivisibleSubset(nums)
    assert l0 == l1
