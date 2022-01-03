from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next: 'ListNode' = None


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(u):
            v = None
            while u is not None:
                u_next = u.next
                u.next = v
                v = u
                u = u_next
            return v

        if head is None or head.next is None:
            return

        slow, u, fast = head, None, head
        while fast is not None and fast.next is not None:
            u = slow
            slow = slow.next
            fast = fast.next.next

        if fast is not None:
            u = slow

        v = reverse(u.next)
        u.next = None

        u = head
        while v is not None:
            u_next = u.next
            u.next = v
            v = v.next
            u.next.next = u_next
            u = u_next


def test_A0():
    lst = ListNode(0, ListNode(1, ListNode(2)))
    lst0 = ListNode(0, ListNode(2, ListNode(1)))
    Solution().reorderList(lst)

    assert lst == lst0


def test_A1():
    lst = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
    lst0 = ListNode(0, ListNode(3, ListNode(1, ListNode(2))))
    Solution().reorderList(lst)

    assert lst == lst0
