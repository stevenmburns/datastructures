from random import gauss
from typing import List

from functools import reduce

from hypothesis import given
from hypothesis.strategies import integers, lists


class SolutionTroll:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        assert len(gas) == len(cost)

        def simulate(start):
            i = start
            tank = 0
            while True:
                tank += gas[i] - cost[i]
                if tank < 0:
                    return False
                i = (i+1) % n
                if i == start:
                    return True

        for i in range(n):
            if simulate(i):
                return i

        return -1


class SolutionAcceptable:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        assert len(gas) == len(cost)

        tank, smallest_i, smallest_tank = 0, 0, None
        for i, delta in enumerate(g - c for g, c in zip(gas, cost)):
            tank += delta
            if smallest_tank is None or tank < smallest_tank:
                smallest_i, smallest_tank = i, tank

        if tank < 0:
            return -1

        return (smallest_i + 1) % n


class SolutionExceeededExpectations:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        assert len(gas) == len(cost)

        def f(s, tup):
            i, (g, c) = tup
            tank, smallest_tank, smallest_i = s
            new_tank = tank + g - c
            if smallest_tank is None or new_tank < smallest_tank:
                return new_tank, new_tank, i
            else:
                return new_tank, smallest_tank, smallest_i

        def g(s):
            tank, _, smallest_i = s
            return -1 if tank < 0 else (smallest_i + 1) % n

        return g(reduce(f, enumerate(zip(gas, cost)), (0, None, None)))


class SolutionOutstanding:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return (lambda s: (-1 if s[0] < 0 else (s[1][1] + 1) % len(gas)))(reduce(
            (lambda s, i: (s[0] + gas[i] - cost[i],
                           min((s[0] + gas[i] - cost[i],
                                i),
                               s[1]))),
            range(1, len(gas)),
            (gas[0] - cost[0],
             (gas[0] - cost[0],
              0))))


class SolutionCheat:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = (i + 1) % len(gas)
        return start


Solution = SolutionOutstanding


def test_A0():
    assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3


def test_A1():
    assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1


def test_A2():
    assert Solution().canCompleteCircuit([3, 1, 1], [1, 2, 2]) == 0


same_len_lists = integers(min_value=1, max_value=100).flatmap(
    lambda n: lists(lists(integers(min_value=0, max_value=10),
                          min_size=n, max_size=n),
                    min_size=2, max_size=2
                    )


)


@ given(same_len_lists)
def test_hypo(pair):
    gas, cost = pair
    print(gas, cost)
    assert Solution().canCompleteCircuit(gas, cost) == SolutionAcceptable().canCompleteCircuit(gas, cost)
