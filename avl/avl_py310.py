from dataclasses import dataclass

from typing import Optional

@dataclass
class AVLTree:
    key : int
    l : Optional['AVLTree'] = None
    r : Optional['AVLTree'] = None
    height : int = 0

    def __call__(self, l=None, r=None):
        self.l = l
        self.r = r
        self.set_height()
        return self

    def __post_init__(self):
        self.set_height()

    @property
    def lheight(self):
        return self.l.height if self.l is not None else 0

    @property
    def rheight(self):
        return self.r.height if self.r is not None else 0

    def set_height(self):
        self.height = 1 + max(self.lheight, self.rheight)
        return self

    def find(self, key):
        """Returns none if key not in tree; Pointer to tree node otherwise"""
        if key == self.key:
            return self
        elif key < self.key:
            return self.l.find(key) if self.l is not None else None
        else:
            return self.r.find(key) if self.r is not None else None

    def rebalance(self):
        assert -2 <= self.rheight - self.lheight <= 2
        match self:
            case AVLTree(_, A, AVLTree(_, AB, B) as b) as a if self.r.lheight <= self.r.rheight and self.rheight > self.lheight + 1:
                return b(a(A, AB), B) 
            case AVLTree(_, A, AVLTree(_, AVLTree(_, AB, BC) as b, C) as c) as a if self.r.lheight > self.r.rheight and self.rheight > self.lheight + 1:
                return b(a(A, AB), c(BC, C))
            case AVLTree(_, AVLTree(_, B, BC) as b, C) as c if self.l.lheight >= self.l.rheight and self.lheight > self.rheight + 1:
                return b(B, c(BC, C))
            case AVLTree(_, AVLTree(_, A, AVLTree(_, AB, BC) as b) as a, C) as c if self.l.lheight < self.l.rheight and self.lheight > self.rheight + 1:
                return b(a(A, AB), c(BC, C))
            case _:
                return self.set_height()

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
                new_tree(self.l, new_tree_r)
            # call with no arguments sets l and r subtrees to null
            return self(), new_tree.rebalance() if new_tree is not None else None
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
            # Need to save because self() will overwrite self.r
            new_tree = self.r
            # call with no arguments sets l and r subtrees to null
            return self(), new_tree

    def check_height(self):
        lh = self.l.check_height() if self.l is not None else 0
        rh = self.r.check_height() if self.r is not None else 0
        assert self.height == 1+max(lh,rh)
        # Balance criteria
        assert -1 <= lh - rh <= 1
        return self.height
