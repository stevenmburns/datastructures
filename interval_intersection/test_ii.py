from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        result = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            l0, r0 = firstList[i]
            l1, r1 = secondList[j]
            if r0 < l1:
                i += 1
            elif r1 < l0:
                j += 1
            else:
                result.append([max(l0, l1), min(r0, r1)])
                if r0 < r1:
                    i += 1
                else:
                    j += 1
        return result
        
        
        

def test_A0():
    assert Solution().intervalIntersection([[1, 3], [5, 6]], [[2, 3], [5, 7]]) == [[2, 3],[5,6]]
    assert Solution().intervalIntersection([[1, 2], [5, 6]], [[3, 4], [7, 8]]) == []
