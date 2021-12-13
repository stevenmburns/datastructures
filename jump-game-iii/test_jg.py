from typing import List

class SolutionTroll:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def next_states(i):
            for off in [arr[i], -arr[i]]:
                if 0 <= i + off < n:
                    yield i + off
                    
        reached = set()
        frontier = { start }    
        while frontier:
            if any(arr[i] == 0 for i in frontier):
                return True
            newfrontier = { j for i in frontier for j in next_states(i) }
            reached = reached.union(frontier)
            frontier = { i for i in newfrontier if i not in reached}
            
        return False

class SolutionAcceptable:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def next_states(i):
            for off in [arr[i], -arr[i]]:
                if 0 <= i + off < n:
                    yield i + off
                    
        reached = set()
        frontier = { start }    
        while frontier:
            if any( arr[i] == 0 for i in frontier):
                return True
            newfrontier = { j for i in frontier for j in next_states(i) }
            reached.update(frontier)

            frontier = newfrontier.difference(reached)
            
        return False

class SolutionExceedsExpectations:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        frontier = { start }    
        while frontier:
            if any( arr[i] == 0 for i in frontier):
                return True
            newfrontier = { i+off for i in frontier for off in [arr[i], -arr[i]] if 0 <= i+off < n}
            for i in frontier:
                assert arr[i] > 0
                arr[i] = -arr[i]
            frontier = {j for j in newfrontier if arr[j] >= 0}  
        return False

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        frontier = { start }    
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
    arr = [4,2,3,0,3,1,2]
    assert Solution().canReach(arr, 5) == True
            
def test_A1():
    arr = [1] * 50000 + [0]
    assert Solution().canReach(arr, 0) == True