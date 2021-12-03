from typing import List
from collections import defaultdict, Counter
from itertools import combinations, product
from bisect import bisect_left, bisect_right

class SolutionTroll:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        tbl = defaultdict(set)
        
        for i,x in enumerate(nums):
            tbl[x].add(i)
        
        n = len(nums)
        
        result = set()
        
        for i,j,k in combinations(range(1,len(nums)),3):
            u = target - nums[i] - nums[j] - nums[k]
            if u in tbl:
                if any(q < i for q in tbl[u].difference({ i,j,k})):
                    result.add( tuple(sorted([u, nums[k], nums[j], nums[i]])))
        
        return [list(fs) for fs in result]

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        histo = Counter(nums)
        result = set()

        if target % 4 == 0:
            cand = target // 4
            if cand in histo:
                if histo[cand] >= 4:
                    result.add( (cand, cand, cand, cand) )

        nums = []
        for k,v in sorted(histo.items()):
            nums.extend([k]*min(3, v))

        lb, ub = bisect_left(nums, target // 2), bisect_right(nums, target // 2)
        print(lb, ub, nums[:lb], nums[ub:])

        pairwise_sums0 = defaultdict(list)
        for i,j in combinations(range(0,ub),2):
            pairwise_sums0[nums[i] + nums[j]].append((i,j))

        pairwise_sums1 = defaultdict(list)
        for i,j in combinations(range(lb,len(nums)),2):
            pairwise_sums1[nums[i] + nums[j]].append((i,j))

        for k0 in pairwise_sums0.keys():
            k1 = target - k0
            if k0 <= k1 and k1 in pairwise_sums1:
                for p, q in product(pairwise_sums0[k0], pairwise_sums1[k1]):

                    quad = p + q
                    if 4 == len(set(quad)):
                        result.add( tuple(sorted([nums[i] for i in quad]))) 
        

        return [list(fs) for fs in result]

def canonize(lst_of_lsts):
    return sorted([sorted(fs) for fs in lst_of_lsts])

def test_A0():
    assert canonize(Solution().fourSum([1,0,-1,0,-2,2], 0)) == canonize([[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]])

def test_A1():
    assert canonize(Solution().fourSum([-1,0,1,2,-1,-4], -1)) == canonize([[-4,0,1,2],[-1,-1,0,1]])