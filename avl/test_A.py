import random

class AVLTree:
    def reuse(self, l=None, r=None):
        self.l = l
        self.r = r
        self.depth = self.compute_depth()
        

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
        if -1 <= self.ldepth - self.rdepth <= 1:
            return self
        else:

            if self.rdepth > self.ldepth + 1:
                assert self.rdepth == self.ldepth + 2
                if self.r.ldepth <= self.r.rdepth: # line
                    a, b, c = self, self.r, self.r.r
                    A, AB, BC, C = self.l, self.r.l, self.r.r.l, self.r.r.r
                else:
                    a, b, c = self, self.r.l, self.r
                    A, AB, BC, C = self.l, self.r.l.l, self.r.l.r, self.r.r

            if self.ldepth > self.rdepth + 1:
                assert self.ldepth == self.rdepth + 2
                if self.l.ldepth >= self.l.rdepth: # line
                    a, b, c = self.l.l, self.l, self
                    A, AB, BC, C  = self.l.l.l, self.l.l.r, self.l.r, self.r
                else:
                    a, b, c = self.l, self.l.r, self
                    A, AB, BC, C = self.l.l, self.l.r.l, self.l.r.r, self.r

            a.reuse(A,  AB)
            c.reuse(BC, C)
            b.reuse(a,  c)

            return b



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
            self.depth = self.compute_depth()

            return new_pointer, self.rebalance()


    def check_depth(self):
        ldepth = self.l.check_depth() if self.l is not None else 0
        rdepth = self.r.check_depth() if self.r is not None else 0
        assert self.depth == 1+max(ldepth,rdepth)

        # Balance criteria
        assert -1 <= ldepth - rdepth <= 1

        return self.depth


    def __str__(self):
        return f"({str(self.l) if self.l is not None else ''}) {self.key} ({str(self.r) if self.r is not None else ''})"


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

