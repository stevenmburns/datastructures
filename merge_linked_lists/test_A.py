# Definition for singly-linked list.

from heapq import heappush, heappop, heapreplace
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ListNode:
    val: int
    next: Optional['ListNode'] = None

    def __lt__(self, other: Optional['ListNode']) -> bool:
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q: List[Optional[ListNode]] = []
        for lst in lists:
            if lst is not None:
                heappush(q, lst)
        root = None
        last = None
        while q:
            if q[0].next is not None:
                lst = heapreplace(q, q[0].next)
            else:
                lst = heappop(q)

            if last is None:
                root = lst
                last = root
            else:
                last.next = lst
                last = last.next
            last.next = None
        return root


def fromList(lst):
    if lst:
        root = ListNode(lst[0])
        last = root
        for x in lst[1:]:
            last.next = ListNode(x)
            last = last.next
        return root
    else:
        return None


def toList(u: Optional[ListNode]):
    x = []
    while u is not None:
        x.append(u.val)
        u = u.next
    return x


def test_A():
    lsts = [fromList([0, 1]), fromList([0])]
    assert toList(Solution().mergeKLists(lsts)) == [0, 0, 1]


def test_B():
    lsts = [fromList([0, 1]), fromList([0]), fromList(
        [0, 1]), fromList([0]), fromList([0, 1])]
    assert toList(Solution().mergeKLists(lsts)) == [0, 0, 0, 0, 0, 1, 1, 1]
