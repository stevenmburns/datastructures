import random

class AVLTree:
    def __init__(self, key, l=None, r=None, depth=1):
        self.key = key
        self.l = l
        self.r = r
        self.depth = depth

    @property
    def ldepth(self):
        return self.l.depth if self.l is not None else 0

    @property
    def rdepth(self):
        return self.r.depth if self.r is not None else 0

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
        def d(x):
            return x.depth if x is not None else 0

        if -1 <= self.ldepth - self.rdepth <= 1:
            return self
        else:

            if self.rdepth > self.ldepth + 1:
                assert self.rdepth == self.ldepth + 2
                assert self.r.ldepth != self.r.rdepth
                if self.r.ldepth < self.r.rdepth: # line
                    a = self
                    b = self.r
                    c = self.r.r
                    A  = self.l
                    AB = self.r.l
                    BC = self.r.r.l
                    C = self.r.r.r

                    a.l = A
                    a.r = AB
                    a.depth = 1+max(d(a.l),d(a.r))
                    c.l = BC
                    c.r = C
                    c.depth = 1+max(d(c.l),d(c.r))
                    b.l = a
                    b.r = c
                    b.depth = 1+max(d(b.l),d(b.r))
                    return b
                else:
                    a = self
                    b = self.r.l
                    c = self.r
                    A  = self.l
                    AB = self.r.l.l
                    BC = self.r.l.r
                    C = self.r.r

                    a.l = A
                    a.r = AB
                    a.depth = 1+max(d(a.l),d(a.r))
                    c.l = BC
                    c.r = C
                    c.depth = 1+max(d(c.l),d(c.r))
                    b.l = a
                    b.r = c
                    b.depth = 1+max(d(b.l),d(b.r))
                    return b

            if self.ldepth > self.rdepth + 1:
                assert self.ldepth == self.rdepth + 2
                assert self.l.ldepth != self.l.rdepth
                if self.l.ldepth > self.l.rdepth: # line
                    c = self
                    b = self.l
                    a = self.l.l

                    A  = self.l.l.l
                    AB = self.l.l.r
                    BC = self.l.r
                    C = self.r

                    a.l = A
                    a.r = AB
                    a.depth = 1+max(d(a.l),d(a.r))
                    c.l = BC
                    c.r = C
                    c.depth = 1+max(d(c.l),d(c.r))
                    b.l = a
                    b.r = c
                    b.depth = 1+max(d(b.l),d(b.r))
                    return b

                else:
                    c = self
                    b = self.l.r
                    a = self.l

                    A  = self.l.l
                    AB = self.l.r.l
                    BC = self.l.r.r
                    C = self.r

                    a.l = A
                    a.r = AB
                    a.depth = 1+max(d(a.l),d(a.r))
                    c.l = BC
                    c.r = C
                    c.depth = 1+max(d(c.l),d(c.r))
                    b.l = a
                    b.r = c
                    b.depth = 1+max(d(b.l),d(b.r))
                    return b

    def add(self, key):
        """Returns existing pointer if already in the tree; other adds and returrns the new Node"""

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
            self.depth = 1+max(self.ldepth, self.rdepth)

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

    tree = AVLTree( 2, AVLTree(0), AVLTree(4), 2)

    assert tree.find(0) is not None
    assert tree.find(2) is not None
    assert tree.find(4) is not None

    assert tree.find(-1) is None
    assert tree.find(1) is None
    assert tree.find(3) is None
    assert tree.find(5) is None

    tree.check_depth()

def test_find2():

    tree = AVLTree( 6, AVLTree(2, AVLTree(0), AVLTree(4), 2), AVLTree(8), 3)

    for x in range(0,10,2):
        assert tree.find(x) is not None

    for x in range(-1,12,2):
        assert tree.find(x) is None

    tree.check_depth()

def test_add():
    lst = list(range(10000))
    #random.shuffle(lst)

    tree = AVLTree(lst[0])
    for x in lst[1:]:
        _, tree = tree.add(x)

    print(tree)

    tree.check_depth()

    for x in lst:
        assert tree.find(x)

    print(tree.depth)
