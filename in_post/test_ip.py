from itertools import product
from typing import List, Optional

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        t = {x: idx for idx, x in enumerate(inorder)}

        def aux(il, iu, pl, pu):
            if il >= iu:
                return None

            x = postorder[pu - 1]
            m = t[x]

            return TreeNode(x,
                            aux(il,  m,  pl,      pl+m-il),
                            aux(m+1, iu, pl+m-il, pu-1))

        return aux(0, len(inorder), 0, len(postorder))


class SolutionTroll:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        m = postorder[-1]

        l = inorder.index(m)

        t = TreeNode(m)
        t.left = self.buildTree(inorder[:l], postorder[:l])
        t.right = self.buildTree(inorder[l+1:], postorder[l:-1])

        return t


class SolutionPoor:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def aux(il, iu, pl, pu):
            assert iu-il == pu-pl
            if il >= iu:
                return None

            m = postorder[pu-1]

            mm = inorder[il:iu].index(m)

            t = TreeNode(m)
            t.left = aux(il, mm+il, pl, mm+pl)
            t.right = aux(il+mm+1, iu, pl+mm, pu-1)

            return t

        return aux(0, len(inorder), 0, len(postorder))


def test_A0():

    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    s = Solution()
    r = s.buildTree(inorder, postorder)
    print(r)
