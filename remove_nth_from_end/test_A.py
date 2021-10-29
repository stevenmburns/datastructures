from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        header = ListNode()
        header.next = head
        u = header
        while u is not None:
            stack.append(u)
            u = u.next

        prev = stack[-n-1]
        curr = prev.next
        prev.next = curr.next
        return header.next

    def toListNode(self, lst):
        header = ListNode()
        last = header
        for x in lst:
            last.next = ListNode(x)
            last = last.next
        return header.next

    def toList(self, l):
        lst = []
        while l is not None:
            lst.append(l.val)
            l = l.next
        return lst


def test_end_to_end():
    l = Solution().toListNode([0, 1, 2])
    assert Solution().toList(l) == [0, 1, 2]


def test_remove():
    l = Solution().toListNode(range(10))
    l = Solution().removeNthFromEnd(l, 5)
    print(Solution().toList(l))
