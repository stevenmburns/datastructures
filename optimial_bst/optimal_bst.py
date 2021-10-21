from itertools import accumulate
import random

class Tree:
    def __init__(self, key, l=None, r=None):
        self.key = key
        self.l = l
        self.r = r

    def __eq__(self, other):
        return other is not None and self.key == other.key and self.l == other.l and self.r == other.r

    def find(self, key, level):
        if key == self.key:
            return self, level
        elif key < self.key:
            if self.l is not None:
                return self.l.find(key, level+1)
            else:
                return None, level
        else:
            if self.r is not None:
                return self.r.find(key, level+1)
            else:
                return None, level

    @staticmethod
    def build(keys, probs):
        
        cprobs = (0,) + tuple(accumulate(probs))

        assert len(keys) == len(probs)

        assert keys == list(sorted(keys))

        costs = {}
        for i in range(len(keys)+1):
            # (0,0),(1,1),(2,2),(3,3)
            costs[(i,i)] = 0, None

        # j in {0,1,2}
        for j in range(len(keys)):
            # i in {0,1,2} for j == 0
            # i in {0,1}   for j == 1
            # i in {0}     for j == 2
            for i in range(len(keys)-j):
                # (0,1),(1,2),(2,3)
                #    (0,2),(1,3)
                #       (0,3)
                ii = i + j + 1

                # probs =  0.3 0.2 0.5
                # keys  =  0   1   2   3  
                # cprobs:  0.0 0.3 0.5 1.0
                # probs between (0,2) cprob[2] - cprob[0]
                # probs[k] = cprobs[k+1] - cprobs[k]

                # for (i,ii) = (0,2) we need (0,0) 0 (1,2); (0,1) 1 (2,2)
                lst = []
                for k in range(i,ii):
                    cand2 = costs[(i,k)][0]    + cprobs[k]  - cprobs[i]   + \
                            costs[(k+1,ii)][0] + cprobs[ii] - cprobs[k+1] + \
                            probs[k]
                    cand = costs[(i,k)][0]    - cprobs[i]   + \
                           costs[(k+1,ii)][0] + cprobs[ii]
                    assert abs(cand - cand2) <= 0.00001
                        
                    #lst.append( (cand, k))
                    lst.append( (cand, Tree(k, costs[(i,k)][1], costs[(k+1,ii)][1])))
                costs[(i,ii)] = min(lst, key=lambda p: p[0])
                
        def aux(lb, ub):
            if lb < ub:
                _, k = costs[(lb,ub)]
                return Tree(k, aux(lb, k), aux(k+1, ub))
            else:
                return None

        print(costs[(0,len(keys))])

        #return aux(0,len(keys))
        return costs[(0,len(keys))]

    def __repr__(self):
        return f'Tree({self.key}, {repr(self.l)}, {repr(self.r)})'

def test_A():
    t = Tree(1, Tree(0), Tree(2)) 
    for x in range(3):
        assert t.find(x,1) is not None

def test_B():

    _, t = Tree.build( [0], [1.0])
    assert t == Tree(0)

    _, t = Tree.build( [0,1], [.3,.7])
    assert t == Tree(1, Tree(0), None)

    _, t = Tree.build( [0,1], [.7,.3])
    assert t == Tree(0, None, Tree(1))

    _, t = Tree.build( [0,1,2], [.3,.2,.5])
    assert t == Tree(2, Tree(0, None, Tree(1)))

def test_C():
    random.seed(47)

    n = 100

    freqs = [ random.randrange(1, 100) for _ in range(n)]
    s = sum(freqs)
    probs = [ x / s for x in freqs]
    keys = list(range(n))

    c, t = Tree.build( keys, probs)

    print( list(zip(keys,freqs)))

    r = 0
    for x,p in zip(keys,probs):
        _, l = t.find(x, 1)
        r += l*p

    print(r)
    assert abs(c-r) <= 0.00001
