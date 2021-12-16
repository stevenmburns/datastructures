from typing import Optional

from dataclasses import dataclass

from collections import deque

@dataclass
class ListNode:
    val: int = 0
    next: Optional['ListNode'] = None


class SolutionCheat:
    def insertionSortList(self, head):
        helper= ListNode(0, head)
        
        while head and head.next:
            if head.next.val > head.val:
                head = head.next
                continue
            
            cur = head.next #the node needs to be inserted
            head.next = head.next.next
            
            #find the inserting position
            pre = helper
            while pre.next and pre.next.val<cur.val:
                pre = pre.next
            
            # inserting node
            cur.next = pre.next
            pre.next = cur

        return helper.next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        header = ListNode()

        def list_contents_reversed(u):
            lst = deque()
            while u is not None:
                lst.appendleft(u.val)
                u = u.next
            return ' '.join(str(x) for x in lst)

        def list_contents(u):
            lst = deque()
            while u is not None:
                lst.append(u.val)
                u = u.next
            return ' '.join(str(x) for x in lst)


        def print_state(sorted, remaining):
            ...
            #print(f"{list_contents_reversed(sorted)} | {list_contents(remaining)}")

        
        while head is not None:
            print_state(header.next, head)

            cursor = header
            while cursor.next is not None and cursor.next.val >= head.val:
                cursor = cursor.next
            head_next = head.next
            head.next = cursor.next
            cursor.next = head
            head = head_next

        print_state(header.next, head)

        result = None
        u = header.next
        while u is not None:
            u_next = u.next
            u.next = result
            result = u
            u = u_next
            
        return result

def test_A0():
    head = ListNode(4, ListNode(3, ListNode(1, ListNode(2))))
    result = Solution().insertionSortList(head)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 4


def almost_sorted(n):
    for i in range(n):
        if i % 2 == 0:
            yield i + 1
        else:
            yield i - 1

def test_sorted():
    n = 40000
    head = None
    for i in reversed(list(almost_sorted(n))):
        head = ListNode(i, head)

    result = Solution().insertionSortList(head)

    for i in range(n):
        assert result.val == i
        result = result.next

    assert result is None

def test_sorted_cheat():
    n = 40000
    head = None
    for i in reversed(list(almost_sorted(n))):
        head = ListNode(i, head)

    result = SolutionCheat().insertionSortList(head)

    for i in range(n):
        assert result.val == i
        result = result.next

    assert result is None    

