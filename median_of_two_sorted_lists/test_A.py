from hypothesis import given, example
import hypothesis.strategies as st

from typing import List

import bisect


class TwoSortedLists:
    def __init__(self, nums1, nums2):
        self.lst0, self.lst1 = (nums1, nums2) if len(
            nums1) >= len(nums2) else (nums2, nums1)
        assert len(self.lst0) >= max(1, len(self.lst1))
        self.total = len(self.lst0) + len(self.lst1)
        self.half = self.total // 2
        # print(self.half, self.lst0, self.lst1)

    def __len__(self):
        return len(self.lst1)+1

    def __getitem__(self, idx):
        if idx < len(self):
            xsplitm1 = idx-1
            ysplit = self.half-idx
            y1cand = 0 <= ysplit < len(self.lst0)
            x0cand = 0 <= xsplitm1 < len(self.lst1)
            return x0cand and y1cand and self.lst1[xsplitm1] > self.lst0[ysplit]
        else:
            raise StopIteration

    def values(self, xsplit, ysplit):
        # print(f'ysplit: {ysplit} y0lst: {self.lst0[:ysplit]} y1lst: {self.lst0[ysplit:]}')
        # print(f'xsplit: {xsplit} x0lst: {self.lst1[:xsplit]} x1lst: {self.lst1[xsplit:]}')

        y0 = [self.lst0[ysplit-1]] if 0 <= ysplit-1 < len(self.lst0) else []
        y1 = [self.lst0[ysplit]] if 0 <= ysplit < len(self.lst0) else []

        x0 = [self.lst1[xsplit-1]] if 0 <= xsplit-1 < len(self.lst1) else []
        x1 = [self.lst1[xsplit]] if 0 <= xsplit < len(self.lst1) else []

        return x0, x1, y0, y1


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tsl = TwoSortedLists(nums1, nums2)

        # print([tsl[i] for i in range(len(tsl))])

        cursor = bisect.bisect(tsl, False)

        xsplit = cursor-1
        ysplit = tsl.half-xsplit

        x0, x1, y0, y1 = tsl.values(xsplit, ysplit)
        # print(f'cursor,x0,x1,y0,y1: {cursor}, {x0}, {x1}, {y0}, {y1} {list(tsl)}')

        if x0 and y1:
            assert x0[0] <= y1[0]
        if y0 and x1:
            assert x1[0] > y0[0]

        # There are up to four things to worry about
        if tsl.total % 2 == 1:
            return min(x1 + y1)
        else:
            return (max(x0 + y0) + min(x1 + y1)) / 2

# @example([0],[])
# @example([0,1,2,3,4],[0,1,2])
# @example([1,3],[2])
# @example([1,3],[2,7])
# @example([1,2],[3,4])
# @example([0,0],[0,0])
# @example([0,0],[1])


@ example([1, 1], [0])
@ given(st.lists(st.sampled_from(range(10)), min_size=1), st.lists(st.sampled_from(range(10)), min_size=0))
def test_hypo(nums1, nums2):
    nums1.sort()
    nums2.sort()

    nums = nums1 + nums2
    nums.sort()

    h = len(nums)
    assert h > 0
    if h % 2 == 1:
        ref = nums[h//2]
    else:
        ref = (nums[h//2-1] + nums[h//2]) / 2

    assert Solution().findMedianSortedArrays(nums1, nums2) == ref


def test_two_sorted1():
    nums1 = [1, 2]
    nums2 = [3, 4]

    tsl = TwoSortedLists(nums1, nums2)

    lst = [tsl[i] for i in range(len(tsl))]
    print(lst)


def test_two_sorted2():
    nums1 = [1, 1]
    nums2 = [0]

    tsl = TwoSortedLists(nums1, nums2)

    lst = [tsl[i] for i in range(len(tsl))]
    print(lst)


def test_two_sorted3():
    nums1 = [0]
    nums2 = [1]

    tsl = TwoSortedLists(nums1, nums2)

    lst = [tsl[i] for i in range(len(tsl))]
    print(lst)


def test_two_sorted4():
    nums1 = [0, 0]
    nums2 = [1, 1]

    tsl = TwoSortedLists(nums1, nums2)

    lst = [tsl[i] for i in range(len(tsl))]
    print(lst)


def test_debug():
    nums1 = [1]
    nums2 = [0]
    nums1 = [1, 2]
    nums2 = [3, 4]

    nums1.sort()
    nums2.sort()

    nums = nums1 + nums2
    nums.sort()

    h = len(nums)
    assert h > 0
    if h % 2 == 1:
        ref = nums[h//2]
    else:
        ref = (nums[h//2-1] + nums[h//2]) / 2

    assert Solution().findMedianSortedArrays(nums1, nums2) == ref
