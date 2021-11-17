from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        count = 0

        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        def aux(node: TreeNode):
            nonlocal count
            if node.left is not None:
                if is_leaf(node.left):
                    count += node.left.val
                else:
                    aux(node.left)

            if node.right is not None:
                aux(node.right)

        if root is not None:
            aux(root)

        return count


def test_A0():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().sumOfLeftLeaves(root) == 24
