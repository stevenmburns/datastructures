from heapq import merge
from dataclasses import dataclass
from typing import List


@dataclass
class TreeNode:
    val: int = 0
    left: 'TreeNode' = None
    right: 'TreeNode' = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(u):
            if u is not None:
                yield from inorder(u.left)
                yield u.val
                yield from inorder(u.right)
        return merge(inorder(root1), inorder(root2))


def test_A0():
    s = Solution()
    assert list(s.getAllElements(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5)),
                                 TreeNode(2, TreeNode(1), TreeNode(3)))) == [1, 1, 2, 2, 3, 3, 4, 5]
