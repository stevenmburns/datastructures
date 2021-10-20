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
                return b.reuse(a.reuse(A,  AB),  B)
            else:
                a, b, c = self, self.r.l, self.r
                A, AB, BC, C = self.l, self.r.l.l, self.r.l.r, self.r.r
                return b.reuse(a.reuse(A,  AB),  c.reuse(BC, C))
        elif self.ldepth > self.rdepth + 1:
            assert self.ldepth == self.rdepth + 2
            if self.l.ldepth >= self.l.rdepth: # line
                b, c = self.l, self
                B, BC, C  = self.l.l, self.l.r, self.r
                return b.reuse(B,  c.reuse(BC, C))
            else:
                a, b, c = self.l, self.l.r, self
                A, AB, BC, C = self.l.l, self.l.r.l, self.l.r.r, self.r
                return b.reuse(a.reuse(A,  AB),  c.reuse(BC, C))
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
        if key == self.key:
            if self.l is None:
                new_tree = self.r
            elif self.r is None:
                new_tree = self.l
            else:
                new_tree, new_tree_r = self.r.remove_leftmost()
                new_tree.reuse(self.l, new_tree_r)
            self.reuse(None,None)
            return self, new_tree.rebalance() if new_tree is not None else None
        elif key < self.key:
            if self.l is not None:
                existing_pointer, self.l = self.l.remove(key)
                return existing_pointer, self.rebalance()
            else:
                return None, self
        else:
            if self.r is not None:
                existing_pointer, self.r = self.r.remove(key)
                return existing_pointer, self.rebalance()
            else:
                return None, self



    def remove_leftmost(self):
        if self.l is not None:
            existing_pointer, self.l = self.l.remove_leftmost()
            return existing_pointer, self.rebalance()
        else:
            new_tree = self.r
            self.reuse(None, None)
            return self, new_tree

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
