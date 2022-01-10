# Definition for singly-linked list.

from typing import List, Optional
from dataclasses import dataclass

from hypothesis import given, example
from hypothesis.strategies import integers, lists


@dataclass
class ListNode:
    val: int = 0
    next: 'ListNode' = None


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        assert head is not None, 'No empty list'

        header = ListNode(0, head)

        slow, fast = header, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        assert fast is None, 'No odd number of nodes'

        def reverse_list(u):
            reverse_head = None
            while u is not None:
                u_next = u.next
                u.next = reverse_head
                reverse_head = u
                u = u_next
            return reverse_head

        def traverse(u):
            while u is not None:
                yield u.val
                u = u.next

        head2 = slow.next
        slow.next = None

        reversed_head2 = reverse_list(head2)

        res = max((a+b for a, b in zip(traverse(head), traverse(reversed_head2))))

        slow.next = reverse_list(reversed_head2)

        return res


def toList(head: Optional[ListNode]) -> List[int]:
    res = []
    while head is not None:
        res.append(head.val)
        head = head.next
    return res


def fromList(l: List[int]) -> Optional[ListNode]:
    if len(l) == 0:
        return None
    head = ListNode(l[0])
    curr = head
    for i in l[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head


@example([1, 100000])
@example([4, 2, 2, 3])
@example([5, 4, 2, 1])
@given(lists(integers(min_value=0, max_value=10), min_size=2, max_size=100).filter(lambda l: len(l) % 2 == 0))
def test_hypo(lst):
    print(lst)
    n = len(lst)
    head = fromList(lst)
    golden = max((lst[i] + lst[n-i-1] for i in range(n//2)))
    assert Solution().pairSum(head) == golden
    assert lst == toList(head)
