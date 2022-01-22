from typing import List
from collections import defaultdict, Counter
from itertools import chain


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        start = 0
        end = n - 1

        reached = set()
        frontier = {start}

        matches = defaultdict(list)
        for i, num in enumerate(arr):
            matches[num].append(i)

        def next_states(i):
            extra = []
            for j in matches[arr[i]]:
                if i != j:
                    yield j
            matches[arr[i]] = []
            for j in chain([i-1, i+1], extra):
                if 0 <= j < n:
                    yield j

        reached = set()
        frontier = {start}
        levels = 0
        while frontier:
            if any(i == end for i in frontier):
                return levels
            newfrontier = {j for i in frontier for j in next_states(i)}
            reached.update(frontier)

            frontier = newfrontier.difference(reached)
            levels += 1

        return levels

        while frontier:
            newfrontier = set()
            for i in frontier:
                off = arr[i]
                if off == 0:
                    return True
                if 0 <= i + off < n:
                    newfrontier.add(i + off)
                if 0 <= i - off < n:
                    newfrontier.add(i - off)
                arr[i] = -off
            frontier = {j for j in newfrontier if arr[j] >= 0}
        return False


def test_A0():
    assert Solution().minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]) == 3


def test_A1():
    assert Solution().minJumps([7]) == 0


def test_A2():
    assert Solution().minJumps([7, 6, 9, 6, 9, 6, 9, 7]) == 1


def test_A3():
    assert Solution().minJumps([11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]) == 3


def test_A4():
    lst = [7]*49999 + [11]
    assert Solution().minJumps(lst) == 2
