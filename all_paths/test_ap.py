from typing import List


class SolutionTroll:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        final = len(graph) - 1

        def aux(path):
            u = path[-1]
            if u == final:
                yield path
            else:
                for v in graph[u]:
                    yield from aux(path + [v])

        return list(aux([0]))


class SolutionAcceptable:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        final = len(graph) - 1

        bedges = [[] for _ in range(len(graph))]
        for u, v in enumerate(graph):
            for vv in v:
                bedges[vv].append(u)

        reached = {}

        def bdfs(v):
            reached[v] = True
            for u in bedges[v]:
                if u not in reached:
                    bdfs(u)

        bdfs(final)

        def aux(path):
            u = path[-1]
            if u in reached:
                if u == final:
                    yield path
                else:
                    for v in graph[u]:
                        yield from aux(path + [v])

        return list(aux([0]))


class SolutionUnknown:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        final = len(graph) - 1

        bedges = [[] for _ in range(len(graph))]
        for u, v in enumerate(graph):
            for vv in v:
                bedges[vv].append(u)

        reached = {}

        def bdfs(v):
            reached[v] = True
            for u in bedges[v]:
                if u not in reached:
                    bdfs(u)

        bdfs(final)

        path = [0]

        def aux():
            nonlocal path
            u = path[-1]
            if u in reached:
                if u == final:
                    yield list(path)
                else:
                    for v in graph[u]:
                        path.append(v)
                        yield from aux()
                        path.pop()

        return list(aux())


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        final = len(graph) - 1

        bedges = [[] for _ in range(len(graph))]
        for u, v in enumerate(graph):
            for vv in v:
                bedges[vv].append(u)

        reached = {}

        def bdfs(v):
            reached[v] = True
            for u in bedges[v]:
                if u not in reached:
                    bdfs(u)

        bdfs(final)

        path = [0]

        def aux():
            nonlocal path
            u = path[-1]
            if u in reached:
                if u == final:
                    yield list(path)
                else:
                    for v in graph[u]:
                        path.append(v)
                        yield from aux()
                        path.pop()

        return aux()


def test_A0():
    """Test all paths from source to destination"""
    res = Solution().allPathsSourceTarget([[1, 2], [3], [3], []])
    assert set(tuple(lst) for lst in res) == set([(0, 1, 3), (0, 2, 3)])


def test_A1():
    m = 24
    n = 3*m + 2
    graph = [[] for _ in range(n)]

    for i in range(3, 3*m+1, 3):
        graph[i-3].append(i-2)
        graph[i-3].append(i-1)
        graph[i-2].append(i)
        graph[i-1].append(i)

    graph[0].append(n-1)

    assert list(Solution().allPathsSourceTarget(graph)) == [[0, n-1]]
