from itertools import combinations

from dataclasses import dataclass
from typing import Optional
@dataclass
class TreeNode:
    val : int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

    max_path_length : Optional[int] = None

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = None
        def post_order( u: TreeNode) -> int: # 
            nonlocal result
            ul = post_order(u.left) if u.left is not None else 0
            ur = post_order(u.right) if u.right is not None else 0
            tmp = u.val + max(0, ul, ur)
            cand = max(tmp, u.val + ul + ur)
            if result is None or result < cand:
                result = cand
            return tmp

        post_order(root)
        return result

def test_A():
    t = TreeNode(2,TreeNode(1), TreeNode(3))
    assert Solution().maxPathSum(t) == 6

def test_B():
    t = TreeNode(-3)
    assert Solution().maxPathSum(t) == -3

def test_C():
    t = TreeNode(9,TreeNode(6),TreeNode(-3,TreeNode(-6),TreeNode(2,TreeNode(2,TreeNode(-6,TreeNode(-6),None),TreeNode(-6)))))
    assert Solution().maxPathSum(t) == 16
    
