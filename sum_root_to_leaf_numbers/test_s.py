
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def aux(u: Optional[TreeNode], prefix: int) -> int:
            count = 0
            new_prefix = prefix * 10 + u.val
            if u.left is None and u.right is None:
                count += new_prefix
            if u.left is not None:
                count += aux(u.left, new_prefix)
            if u.right is not None:
                count += aux(u.right, new_prefix)
            return count

        if root is not None:
            return aux(root, 0)
        else:
            return 0


def test_A0():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert Solution().sumNumbers(root) == 44


def test_A1():
    assert Solution().sumNumbers(None) == 0


def test_A2():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().sumNumbers(root) == 25


def test_A3():
    root = TreeNode(1, TreeNode(2), None)
    assert Solution().sumNumbers(root) == 12
