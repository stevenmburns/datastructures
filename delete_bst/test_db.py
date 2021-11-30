from dataclasses import dataclass

from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


def remove(root, key):
    if root is None:
        return None, None
    if key == root.val:
        if root.left is None:
            new_tree = root.right
        elif root.right is None:
            new_tree = root.left
        else:
            new_tree, new_tree_r = remove_leftmost(root.right)
            new_tree.left, new_tree.right = root.left, new_tree_r
        root.left, root.right = None, None
        return root, new_tree
    elif key < root.val:
        if root.left is not None:
            existing_pointer, root.left = remove(root.left, key)
            return existing_pointer, root
        else:
            return None, root
    else:
        if root.right is not None:
            existing_pointer, root.right = remove(root.right, key)
            return existing_pointer, root
        else:
            return None, root


def remove_leftmost(root):
    if root.left is not None:
        existing_pointer, root.left = remove_leftmost(root.left)
        return existing_pointer, root
    else:
        new_tree = root.right
        root.left, root.right = None, None
        return root, new_tree


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return remove(root, key)[1]


def test_remove_leftmost():
    tree = TreeNode(5, TreeNode(4, None, None), TreeNode(6, None, None))
    print(f"{repr(tree)}")

    four, tree_r = remove_leftmost(tree.right)

    print(f"{repr(four)}, {repr(tree_r)}")


def test_remove0():
    tree = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4)), TreeNode(8))
    six, new_tree = remove(tree, 6)

    print(f"{str(six)}, {str(new_tree)}")


def test_remove1():
    tree = TreeNode(3, TreeNode(1, TreeNode(0), None), None)

    print(str(tree))
    one, new_tree = remove(tree, 1)

    print(f"{str(one)}, {str(new_tree)}")


def test_remove2():
    tree = TreeNode(3, TreeNode(0, None, TreeNode(1, None, TreeNode(2, None, None))), TreeNode(
        5, TreeNode(4, None, None), TreeNode(6, None, None)))

    print(f"{repr(tree)}")

    three, new_tree = remove(tree, 3)

    print(f"{repr(three)}, {repr(new_tree)}")


def test_remove2a():
    tree = TreeNode(3, TreeNode(0, None, None), TreeNode(
        5, TreeNode(4, None, None), TreeNode(6, None, None)))

    print(f"{repr(tree)}")

    three, new_tree = remove(tree, 3)

    print(f"{repr(three)}, {repr(new_tree)}")
