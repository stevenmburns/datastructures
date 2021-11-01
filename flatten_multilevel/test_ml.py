
from typing import Optional, Any
from dataclasses import dataclass
import pytest

# Definition for a Node.


@dataclass
class Node:
    val: Any = None
    prev: Optional['Node'] = None
    next: Optional['Node'] = None
    child: Optional['Node'] = None


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        header = Node()
        cursor = header

        def aux(u: Node):
            nonlocal cursor
            while u is not None:
                u_nxt = u.next
                u_child = u.child
                cursor.next = u
                u.prev = cursor
                u.child = None
                u.next = None
                cursor = u
                if u_child is not None:
                    aux(u_child)
                u = u_nxt

        aux(head)
        if header.next:
            header.next.prev = None
            return header.next
        else:
            return None


def check(l):
    if l:
        assert l.prev is None
        while l.next is not None:
            assert l == l.next.prev
            l = l.next


def fromList(lst):
    header = Node()
    last = header

    def build(x):
        if type(x) is tuple:
            (val, child) = x
            u = Node(val, None, None, fromList(child))
        else:
            u = Node(x, None, None, None)
        return u

    for x in lst:
        u = build(x)
        u.prev = last
        last.next = u
        last = u

    if header.next is not None:
        header.next.prev = None

    return header.next


def toList(u: Optional[Node]):
    check(u)
    x = []
    while u is not None:
        if u.child is not None:
            x.append((u.val, toList(u.child)))
        else:
            x.append(u.val)
        u = u.next
    return x


def test_end_to_end0():
    lst = [1, 2, (3, [30, (31, [310, 311]), 32]), 4, 5, 6, 7]
    head = fromList(lst)
    assert lst == toList(head)


def test_A0():
    lst = [1, 2]
    head = fromList(lst)
    assert [1, 2] == toList(Solution().flatten(head))


def test_A1():
    lst = [1, 2, (3, [30, (31, [310, 311]), 32]), 4, 5, 6, 7]
    head = fromList(lst)
    assert [1, 2, 3, 30, 31, 310, 311, 32, 4, 5,
            6, 7] == toList(Solution().flatten(head))


def test_A2():
    lst = [(0, []), (1, [10])]
    head = fromList(lst)
    assert [0, 1, 10] == toList(Solution().flatten(head))
