# Definition for singly-linked list.

from typing import List, Optional
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: 'ListNode' = None


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow, fast, prev = head, head, None

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        reverse_head = None
        while slow is not None:
            temp = slow.next
            slow.next = reverse_head
            reverse_head = slow
            slow = temp

        u0, u1 = head, reverse_head
        m = None
        while u0 is not None and u1 is not None:
            cand = u0.val + u1.val
            if m is None or m < cand:
                m = cand
            u0, u1 = u0.next, u1.next

        return m


def test_A0():
    assert Solution().pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1))))) == 6


def test_A1():
    assert Solution().pairSum(ListNode(4, ListNode(2, ListNode(2, ListNode(3))))) == 7


def test_A2():
    assert Solution().pairSum(ListNode(1, ListNode(100000))) == 100001
