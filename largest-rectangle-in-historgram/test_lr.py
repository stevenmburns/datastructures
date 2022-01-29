from curses.ascii import SO


from typing import List
from itertools import chain


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        print('====')

        s, max_area = [], 0
        for i,  y in enumerate(chain(heights, [0])):
            print('top of loop', i, y, s, max_area)

            news = []
            old_endy = None
            for j in range(len(s)):
                startx, endy = s[j]
                max_area = max(max_area, (i-startx)*endy)
                new_endy = min(endy, y)
                if old_endy is None or new_endy > old_endy:
                    news.append((startx, new_endy))
                old_endy = new_endy

            s = news

            if not s or y > s[-1][1]:
                s.append((i, y))

        return max_area


def test_A0():
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10


def test_A1():
    assert Solution().largestRectangleArea([2, 4]) == 4


def test_A3():
    assert Solution().largestRectangleArea([2, 1, 1]) == 3


def test_A2():
    assert Solution().largestRectangleArea([2, 1, 2]) == 3


def test_A4():
    assert Solution().largestRectangleArea([1]) == 1


def test_A5():
    n = 10
    assert Solution().largestRectangleArea(list(range(n))) == (n//2)**2


def test_A6():
    assert Solution().largestRectangleArea([0, 9]) == 9
