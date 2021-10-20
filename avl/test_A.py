import random

from avl import AVLTree

def test_remove_leftmost():
    tree = AVLTree(5, AVLTree(4, None, None), AVLTree(6, None, None))
    print(f"{repr(tree)}")

    four, tree_r = tree.r.remove_leftmost()
    
    print(f"{repr(four)}, {repr(tree_r)}")


def test_remove0():
    tree = AVLTree( 6, AVLTree(2, AVLTree(0), AVLTree(4)), AVLTree(8))    
    six, new_tree = tree.remove(6)

    print(f"{str(six)}, {str(new_tree)}")

def test_remove1():
    tree = AVLTree( 3, AVLTree(1, AVLTree(0), None), None)    

    print(str(tree))
    one, new_tree = tree.remove(1)

    print(f"{str(one)}, {str(new_tree)}")

def test_remove2():
    tree = AVLTree(3, AVLTree(0, None, AVLTree(1, None, AVLTree(2, None, None))), AVLTree(5, AVLTree(4, None, None), AVLTree(6, None, None)))

    print(f"{repr(tree)}")

    three, new_tree = tree.remove(3)

    print(f"{repr(three)}, {repr(new_tree)}")

def test_remove2a():
    tree = AVLTree(3, AVLTree(0, None, None), AVLTree(5, AVLTree(4, None, None), AVLTree(6, None, None)))

    print(f"{repr(tree)}")

    three, new_tree = tree.remove(3)

    print(f"{repr(three)}, {repr(new_tree)}")


def test_find():

    tree = AVLTree( 2, AVLTree(0), AVLTree(4))

    assert tree.find(0) is not None
    assert tree.find(2) is not None
    assert tree.find(4) is not None

    assert tree.find(-1) is None
    assert tree.find(1) is None
    assert tree.find(3) is None
    assert tree.find(5) is None

    tree.check_depth()

def test_find2():

    tree = AVLTree( 6, AVLTree(2, AVLTree(0), AVLTree(4)), AVLTree(8))

    for x in range(0,10,2):
        assert tree.find(x) is not None

    for x in range(-1,12,2):
        assert tree.find(x) is None

    tree.check_depth()

def test_add():
    lst = list(range(10000))
    random.shuffle(lst)

    tree = AVLTree(lst[0])
    for x in lst[1:]:
        _, tree = tree.add(x)


    tree.check_depth()

    for x in lst:
        assert tree.find(x)

def test_add_remove():
    lst = list(range(10000))
    random.shuffle(lst)

    tree = AVLTree(lst[0])
    for x in lst[1:]:
        _, tree = tree.add(x)


    tree.check_depth()

    for x in lst:
        node, tree = tree.remove(x)
        assert node is not None
        assert node.key == x
        assert tree is None or tree.find(x) is None

    assert tree is None

