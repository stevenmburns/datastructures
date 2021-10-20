import random

class AVLTree:
    def reuse(self, l=None, r=None):
        self.l = l
        self.r = r
        self.depth = self.compute_depth()
        return self

    def __init__(self, key, l=None, r=None):
        self.key = key
        self.reuse(l, r)

    @property
    def ldepth(self):
        return self.l.depth if self.l is not None else 0

    @property
    def rdepth(self):
        return self.r.depth if self.r is not None else 0

    def compute_depth(self):
        return 1 + max(self.ldepth, self.rdepth)

    def find(self, key):
        """Returns none if key not in tree; Pointer to tree node otherwise"""
        if key == self.key:
            return self
        elif key < self.key:
            if self.l is not None:
                return self.l.find(key)
        else:
            if self.r is not None:
                return self.r.find(key)
        return None


    def rebalance(self):
        if self.rdepth > self.ldepth + 1:
            assert self.rdepth == self.ldepth + 2
            if self.r.ldepth <= self.r.rdepth: # line
                a, b = self, self.r
                A, AB, B = self.l, self.r.l, self.r.r
                a.reuse(A,  AB)
                return b.reuse(a,  B)
            else:
                a, b, c = self, self.r.l, self.r
                A, AB, BC, C = self.l, self.r.l.l, self.r.l.r, self.r.r
                a.reuse(A,  AB)
                c.reuse(BC, C)
                return b.reuse(a,  c)
        elif self.ldepth > self.rdepth + 1:
            assert self.ldepth == self.rdepth + 2
            if self.l.ldepth >= self.l.rdepth: # line
                b, c = self.l, self
                B, BC, C  = self.l.l, self.l.r, self.r
                c.reuse(BC, C)
                return b.reuse(B,  c)
            else:
                a, b, c = self.l, self.l.r, self
                A, AB, BC, C = self.l.l, self.l.r.l, self.l.r.r, self.r
                a.reuse(A,  AB)
                c.reuse(BC, C)
                return b.reuse(a,  c)
        else:
            self.depth = self.compute_depth()
            return self

    def add(self, key):
        """Returns a pair:
                first: existing pointer if already in the tree; otherwise new node
                second: original tree if key already in tree; otherwise new tree with added node
"""

        if key == self.key:
            return self, self
        else:
            if key < self.key:
                if self.l is not None:
                    new_pointer, self.l = self.l.add(key)
                else:
                    new_pointer = self.l = AVLTree(key)
            else:
                if self.r is not None:
                    new_pointer, self.r = self.r.add(key)
                else:
                    new_pointer = self.r = AVLTree(key)

            return new_pointer, self.rebalance()

    def remove(self, key):
        print(f"remove {key}")
        if key == self.key:
            print(f"found {key} == {self.key}")
            existing_pointer, new_tree = self, None
        else:
            if key < self.key:
                print(f"left {key} < {self.key}")
                if self.l is not None:
                    existing_pointer, self.l = self.l.remove(key)
                    return existing_pointer, self.rebalance()
                else:
                    existing_pointer, new_tree = None, self
            else:
                print(f"right {key} > {self.key}")
                if self.r is not None:
                    existing_pointer, self.r = self.r.remove(key)
                    return existing_pointer, self.rebalance()
                else:
                    existing_pointer, new_tree = None, self

        if existing_pointer is None:
            return None, self
        else:
            assert key == existing_pointer.key

            if self.l is None:
                new_tree = self.r
            elif self.r is None:
                new_tree = self.l
            else:
                print(f'self.r {repr(self.r)}')

                new_tree, new_tree_r = self.r.remove_leftmost()

                print(f'new_tree: {repr(new_tree)} new_tree_r: {repr(new_tree_r)}')

                new_tree.reuse(self.l, new_tree_r)

            #print('SMB', str(new_tree))

            existing_pointer.reuse(None,None)
                
            rebalanced_new_tree = new_tree.rebalance() if new_tree is not None else None

            #print(f'returning {str(existing_pointer)} {str(rebalanced_new_tree)}')

            return existing_pointer, rebalanced_new_tree


    def remove_leftmost(self):
        if self.l is not None:
            existing_pointer, self.l = self.l.remove_leftmost()
            return existing_pointer, self.rebalance()
        else:
            existing_pointer, new_tree = self, self.r
            existing_pointer.reuse(None, None)

            return existing_pointer, new_tree

    def check_depth(self):
        ldepth = self.l.check_depth() if self.l is not None else 0
        rdepth = self.r.check_depth() if self.r is not None else 0
        assert self.depth == 1+max(ldepth,rdepth)

        # Balance criteria
        assert -1 <= ldepth - rdepth <= 1

        return self.depth


    def __str__(self):
        return f"({str(self.l) if self.l is not None else ''}) {self.key} ({str(self.r) if self.r is not None else ''})"

    def __repr__(self):
        return f"AVLTree({self.key}, {self.l.__repr__()}, {self.r.__repr__()})"


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
    lst = list(range(100))
    random.shuffle(lst)

    tree = AVLTree(lst[0])
    for x in lst[1:]:
        _, tree = tree.add(x)


    tree.check_depth()

    for x in lst:
        print(f"Removing {x}, {tree.__repr__()}")
        node, tree = tree.remove(x)
        print(str(tree))
        assert node is not None
        assert node.key == x
        assert tree is None or tree.find(x) is None

    assert tree is None

