from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        fedges = {}
        for i in range(numCourses):
            fedges[i] = []

        for c, p in prerequisites:
            fedges[p].append(c)

        order = deque()
        visited = set()
        labeled = set()

        def dfs(u):
            visited.add(u)
            labeled.add(u)

            for v in fedges[u]:
                if v in labeled:
                    print(f'{u} -> {v} closes a cycle')
                    return True
                elif v not in visited:
                    if dfs(v):
                        return True

            labeled.discard(u)
            order.appendleft(u)

            return False

        for u in range(numCourses):
            labeled.clear()
            if u not in visited:
                if dfs(u):
                    return []

        return list(order)


def test_A0():
    numCourses = 2
    prerequisites = []
    assert Solution().findOrder(numCourses, prerequisites) in [[0, 1], [1, 0]]


def test_A1():
    numCourses = 2
    prerequisites = [[1, 0]]
    assert Solution().findOrder(numCourses, prerequisites) == [0, 1]


def test_A2():
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    assert Solution().findOrder(numCourses, prerequisites) == []
