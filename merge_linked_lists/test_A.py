# Definition for singly-linked list.

from dataclasses import dataclass
from typing import Optional, List

@dataclass
class ListNode:
    val : int
    next : Optional['ListNode'] = None

class Pair:
    def __init__(self, val, lst):
        self.val = val
        self.lst = lst
        
    def __eq__(self, other):
        return self.val == other.val
    
    def __lt__(self, other):
        return self.val < other.val
    

from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        for lst in lists:
            if lst is not None:
                heappush(q, Pair(lst.val, lst))
        root = None
        last = None        
        while q:
            lst = heappop(q).lst
            if lst.next is not None:
                heappush(q, Pair(lst.next.val, lst.next))
            if last is None:
                root = lst
                last = root
            else:
                last.next = lst
                last = last.next
            last.next = None
        return root

 

    
def fromList( lst):
    if lst:
        root = ListNode(lst[0])
        last = root
        for x in lst[1:]:
            last.next = ListNode(x)
            last = last.next
        return root
    else:
        return None


def toList( u : Optional[ListNode]):
    x = []
    while u is not None:
        x.append(u.val)
        u = u.next
    return x

def test_A():
    lsts = [fromList([0,1]),fromList([0])]
    assert toList(Solution().mergeKLists(lsts)) == [0,0,1]
    
