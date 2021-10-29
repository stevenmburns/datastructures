import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        cc = collections.Counter(nums)
        nums = []
        for k, v in cc.items():
            for _ in range(min(3, v)):
                nums.append(k)
        nums.sort()
        print(nums)
        tbl = collections.defaultdict(list)
        for idx, v in enumerate(nums):
            tbl[v].append(idx)

        for k in tbl.keys():
            tbl[k] = max(tbl[k])

        print(tbl)

        result = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            for j in range(i+1, len(nums)):
                cand = -(nums[i] + nums[j])
                if cand in tbl:
                    if tbl[cand] > j:
                        c = collections.Counter([nums[i], nums[j], cand])
                        result.add(frozenset(set(c.items())))
        print(result)
        lstlst = []
        for s in result:
            lst = []
            for a, b in s:
                for _ in range(b):
                    lst.append(a)
            lstlst.append(lst)
        return lstlst


def test_A():
    nums = [-1, 0, 1, 2, -1, -4]
    print(nums)
    print(Solution().threeSum(nums))


def test_B():
    nums = []
    nums.extend(0 for _ in range(1000))
    nums.extend(1 for _ in range(1000))
    nums.extend(-1 for _ in range(1000))
    print(Solution().threeSum(nums))
