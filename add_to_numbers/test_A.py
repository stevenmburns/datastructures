from typing import Optional

from dataclasses import dataclass

@dataclass
class ListNode:
    val : int = 0
    next : Optional['ListNode'] = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        header = ListNode()
        last = header
        carry = 0
        while l1 is not None or l2 is not None:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            cand = v1 + v2 + carry
            last.next = ListNode( cand % 10)
            last = last.next
            carry = cand // 10
                
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
                
        if carry == 1:
            last.next = ListNode( 1)
            last = last.next

        return header.next
    
    def toListNode(self, lst):
        header = ListNode()
        last = header
        for x in lst:
            last.next = ListNode(x)
            last = last.next
        return header.next

    def toList(self, l):
        result = []
        while l is not None:
            result.append(l.val)
            l = l.next
        return result

def test_in_out():
    lst = [0,1,2]
    l = Solution().toListNode(lst)
    assert lst == Solution().toList(l)

def test_add():
    l1 = Solution().toListNode([0,1,2])
    l2 = Solution().toListNode([9,8,9])
    l = Solution().addTwoNumbers(l1, l2)
    assert [9,9,1,1] == Solution().toList(l)

def test_add2():
    l1 = Solution().toListNode([9,9,9,9,9,9,9])
    l2 = Solution().toListNode([9,9,9,9])
    l = Solution().addTwoNumbers(l1, l2)
    assert [8,9,9,9,0,0,0,1] == Solution().toList(l)
    
