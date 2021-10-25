from typing import List

import bisect

class TwoSortedLists:
    def __init__(self, nums1, nums2):
        self.lst0, self.lst1 = (nums1, nums2) if len(nums1) >= len(nums2) else (nums2, nums1)
        assert len(self.lst0) >= max(1,len(self.lst1))
        self.total = len(self.lst0) + len(self.lst1)
        self.half = self.total // 2
        print(self.half,self.lst0, self.lst1)

    def __len__(self):
        return len(self.lst1)

    def __getitem__(self, idx):
        return self.half-idx < len(self.lst0) and self.lst1[idx] > self.lst0[self.half-idx]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tsl = TwoSortedLists( nums1, nums2)
        cursor = bisect.bisect( tsl, False)

        ysplit = tsl.half-cursor+1
        print( f'y0lst: {tsl.lst0[:ysplit]} y1lst: {tsl.lst0[ysplit:]}')

        xsplit = cursor-1
        print( f'x0lst: {tsl.lst1[:xsplit]} x1lst: {tsl.lst1[xsplit:]}')

        if cursor == 0:
            print( f'cursor: {cursor} {list(tsl)}')

            # lst0 <= lst1
            if tsl.total % 2 == 1:
                # [0,1,2] + [3,4]
                #      ^ half 
                return tsl.lst0[tsl.half]
            else:

                if len(tsl.lst0) == len(tsl.lst1):
                    # [0,1] + [2,3]
                    #          ^ half 
                    return (tsl.lst0[-1] + tsl.lst1[0]) / 2
                else:
                    # [0,1,2] + [3]
                    #      ^ half 
                    return (tsl.lst0[tsl.half-1] + tsl.lst0[tsl.half]) / 2
            
        elif cursor == len(tsl):
            print( f'cursor: {cursor} {list(tsl)}')

            # lst1 <= lst0
            if tsl.total % 2 == 1:
                # [0,1] + [2,3,4]
                #          ^ half 
                return tsl.lst0[tsl.half-len(tsl.lst1)]
            else:
                if len(tsl.lst0) == len(tsl.lst1):
                    # [0,1] + [2,3]
                    #          ^ half 
                    return (tsl.lst1[-1] + tsl.lst0[0]) / 2
                else:
                    # [0] + [1,2,3]
                    #          ^ half 
                    return (tsl.lst0[tsl.half-len(tsl.lst1)-1] + tsl.lst0[tsl.half-len(tsl.lst1)]) / 2


        y0 = [tsl.lst0[ysplit-1]] if 0 <= ysplit-1 < len(tsl.lst0) else []
        y1 = [tsl.lst0[ysplit]] if 0 <= ysplit < len(tsl.lst0) else []

        x0 = [tsl.lst1[xsplit-1]] if 0 <= xsplit-1 < len(tsl.lst1) else []
        x1 = [tsl.lst1[xsplit]] if 0 <= xsplit < len(tsl.lst1) else []

        print( f'cursor,x0,x1,y0,y1: {cursor}, {x0}, {x1}, {y0}, {y1} {list(tsl)}')

        if x0 and y1:
            assert x0[0] <= y1[0]
        if y0 and x1:
            assert x1[0] >=  y0[0]

        # There are up to four things to worry about
        if tsl.total % 2 == 1:
            return min(x1 + y1)
        else:
            return (max(x0 + y0) + min(x1 + y1)) / 2


def test_debug():
    # 0,1:2,3,4
    # 0,1:2
    # 0,0,1,1:2,2,3,4

    nums1 = [0, 1, 2, 3, 4]
    nums2 = [0, 1, 2]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 1.5

def test_three():
    nums1 = [1, 3]
    nums2 = [2]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2

def test_four():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5

def test_four_zeros():
    nums1 = [0, 0]
    nums2 = [0, 0]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 0

def test_zero_one():
    nums1 = [0 for _ in range(2)]
    nums2 = [1 for _ in range(1)]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 0

def test_one_zero():
    nums1 = [1 for _ in range(2)]
    nums2 = [0 for _ in range(1)]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 1
