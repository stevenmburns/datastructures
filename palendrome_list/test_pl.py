from typing import Optional, Tuple

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        c = self.count(head)
        l1, l2 = self.split(head, c//2)
        l2 = self.reverse(l2)
        while l1 is not None and l2 is not None:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return True

    def count(self, head: Optional[ListNode]) -> int:
        c = 0
        while head is not None:
            c += 1
            head = head.next
        return c

    def split(self, head: Optional[ListNode], k: int) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        header = ListNode()
        header.next = head
        u = header
        for i in range(k):
            u = u.next
        tmp = u.next
        u.next = None
        return header.next, tmp

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = None

        while head is not None:
            tmp = head.next
            head.next = newhead
            newhead = head
            head = tmp

        return newhead


def fromList(lst):
    header = ListNode()
    last = header
    for x in lst:
        last.next = ListNode(x)
        last = last.next
    return header.next


def toList(u: Optional[ListNode]):
    x = []
    while u is not None:
        x.append(u.val)
        u = u.next
    return x


def test_end_to_end():
    lst = [1, 2, 3, 2, 1]
    l = fromList(lst)
    assert lst == toList(l)


def test_split():
    k = 3
    lst = [1, 2, 3, 2, 1]
    l = fromList(lst)
    (l1, l2) = Solution().split(l, k)
    assert toList(l1) == lst[:k]
    assert toList(l2) == lst[k:]


def test_count():
    lst = [1, 2, 3, 2, 1]
    assert Solution().count(fromList(lst)) == 5


def test_A0():
    lst = [1, 2, 3, 2, 1]
    l = fromList(lst)
    assert Solution().isPalindrome(l) == True
