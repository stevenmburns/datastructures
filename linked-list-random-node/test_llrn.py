from typing import Optional
from dataclasses import dataclass
from collections import defaultdict, Counter
import random
import math


@dataclass
class ListNode:
    val: int = 0
    next: Optional['ListNode'] = None


class SolutionBatch:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        assert head is not None
        self.n = 0
        cursor = self.head
        while cursor is not None:
            self.n += 1
            cursor = cursor.next

        self.batch = max(1, int(math.sqrt(self.n)))
        self.batch = self.n
        print(f'batch: {self.batch}')

        self.genBatch()

    def genBatch(self):

        cache = defaultdict(list)

        for i in range(self.batch):
            cache[random.randrange(self.n)].append(i)

        self.q = [None for _ in range(self.batch)]

        cursor = self.head
        i = 0
        while cursor is not None:
            if i in cache:
                for j in cache[i]:
                    self.q[j] = cursor.val
            cursor = cursor.next
            i += 1

        self.idx = 0

    def getRandom(self) -> int:
        if self.idx == self.batch:
            self.genBatch()
        result = self.q[self.idx]
        self.idx += 1
        return result


class SolutionResevoirSampling:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result, cur, idx = self.head, self.head, 0
        while cur:
            if random.randrange(idx+1) == 0:
                result = cur
            cur = cur.next
            idx += 1
        return result.val


Solution = SolutionBatch


def test_A0():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    sol = Solution(head)
    assert sol.getRandom() in [1, 2, 3, 4, 5]
    assert sol.getRandom() in [1, 2, 3, 4, 5]


def test_A1():
    m = 10000
    n = 100000
    header = ListNode()
    cursor = header
    for i in range(m):
        cursor.next = ListNode(i)
        cursor = cursor.next
    head = header.next
    sol = Solution(head)

    histo = Counter(sol.getRandom() for _ in range(n))
    print(histo.most_common(10))
